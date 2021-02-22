from socket import *
import subprocess
Server_IP=('192.168.0.101',8000)
phone=socket(AF_INET,SOCK_STREAM)
phone.bind(Server_IP)
phone.listen(5)
while True:
    print('开始接受客户端连接')
    conn,addr=phone.accept()
    print("双向链接:",conn)
    print("客户端地址:",addr)
    while True:
        try:
         msg=conn.recv(1024)
         if not msg:
            continue
         else:
             print("收到的命令是:",msg)
         #执行命令得到命令的运行结果cmd_res
         res=subprocess.Popen(msg.decode('utf-8'),shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
         err=res.stderr.read()
         if err:
             cmd_res=err            #bytes形式
         else:
             cmd_res= res.stdout.read()     #bytes形式
             if not cmd_res:
                cmd_res=('这是命令啊，老铁'.encode('gbk'))
         conn.send(cmd_res)
        except Exception:
            break
    conn.close()
phone.close()