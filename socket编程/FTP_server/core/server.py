import socketserver
import json,configparser,os
from conf import  settings
STATUS_CODE  = {

    250 : "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251 : "Invalid cmd ",
    252 : "Invalid auth data",
    253 : "Wrong username or password",
    254 : "Passed authentication",
    255 : "Filename doesn't provided",
    256 : "File doesn't exist on server",
    257 : "ready to send file",
    258 : "md5 verification",

    800 : "the file exist,but not enough ,is continue? ",
    801 : "the file exist !",
    802 : " ready to receive datas",

    900 : "md5 valdate success"

}
class ServerHandle(socketserver.BaseRequestHandler):
    #运行自定义hadle方法即开启服务
    def handle(self):
        while 1:
            #request相当于conn即conn.recv
            data=self.request.recv(1024).strip()
            data=json.loads(data.decode("utf-8"))
            if data.get('action'):
                if hasattr(self,data.get('action')):
                    func=getattr(self,data.get('action'))
                    func(**data)
                else:
                    print('不存在这个aciton')
            else:
                exit('aciton不能为空')
            #取客户端请求过来的账号、密码
    def Login(self,**data):
        username=data['username']
        passwd=data['password']
        user = self.anthenticate(username,passwd)
        if user:
            self.send_response(254)
        else:
            self.send_response(253)

    def send_response(self,statu_code):
        response={"status_code":statu_code}

        self.request.sendall(json.dumps(response).encode('utf-8'))

    #验证账号、密码的准确性
    def anthenticate(self,username,passwd):
        cfg=configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)
        if username in cfg.sections():
        #校验密码是否正确
            if cfg[username]['password']==passwd:
                    self.user=username
                        #拼接文件路径+home+用户名
                    self.mainPath=os.path.join(settings.BASE_DIR,"home",self.user)
                    print('sucess')
                    return username


    def put(self,**data):
        print("data",data)
        file_name=data.get("file_name")
        file_size=data.get("file_size")
        target_path=data.get("target_path")
        #拼接路径+目标路径+文件名
        abs_path=os.path.join(self.mainPath,target_path,file_name)

         ##########################################
        has_received=0
        #服务端文件是否存在
        if os.path.exists(abs_path):
            #统计该文件大小
            file_has_size=os.stat(abs_path).st_size
            #比较文件与客户端发送过来同名文件大小
            if file_has_size<file_size:
                #断点续传
                self.request.sendall("800".encode("utf8"))
                choice=self.request.recv(1024).decode("utf8")
                if choice=="Y":
                    self.request.sendall(str(file_has_size).encode("utf8"))
                    has_received+=file_has_size
                    f=open(abs_path,"ab")
                else:
                    f=open(abs_path,"wb")

            else:
                self.request.sendall("801".encode("utf8"))
                return

        else:
            self.request.sendall("802".encode("utf8"))
            f = open(abs_path, "wb")


        while has_received<file_size:
            #如果客户端断了，Windows系统用异常处理
            try:
                data=self.request.recv(1024)
            #Linux用if not data:
                    #continue
            except Exception as e:
                break
            f.write(data)
            has_received+=len(data)

        f.close()


    def ls(self,**data):

        file_list=os.listdir(self.mainPath) #路径下的文件并以列表展示

        file_str="\n".join(file_list)
        if not len(file_list):
            file_str="<empty dir>"
        self.request.sendall(file_str.encode("utf8"))



    def cd(self,**data):

        dirname=data.get("dirname")

        if dirname=="..":
            self.mainPath=os.path.dirname(self.mainPath)
        else:

             self.mainPath=os.path.join(self.mainPath,dirname)

        self.request.sendall(self.mainPath.encode("utf8"))



    def mkdir(self,**data):

        dirname=data.get("dirname")

        path=os.path.join(self.mainPath,dirname)

        if not os.path.exists(path):
            if "/" in dirname:
                os.makedirs(path)
            else:
                os.mkdir(path)
            self.request.sendall("create success".encode("utf8"))
        else:
            self.request.sendall("dirname exist".encode("utf8"))