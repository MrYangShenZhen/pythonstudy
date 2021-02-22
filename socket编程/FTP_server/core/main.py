import optparse,socketserver
from conf import settings
from core import server
class ArgvHandler():
        def __init__(self):
            self.op=optparse.OptionParser()
            self.op.add_option("-s","--s",dest='server')
            self.op.add_option('-P','--port',dest='port')
            self.options,self.args=self.op.parse_args()
            print(self.options)#规范过的放在这个字典
            print(self.args)#没规范的放这里
            self.verify_args(self.options,self.args)
        def verify_args(self,options,args):
            if args:
                cmd =args[0]
                if hasattr(self,cmd):#反射在类里面找实例的方法
                    func=getattr(self,cmd)
                    func()
            else:
                print("请输入start")
        def start(self,):
            print('服务器开始工作')
            s=socketserver.ThreadingTCPServer((settings.ip,settings.port),server.ServerHandle)
            s.serve_forever()
