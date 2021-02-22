import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is: ',self.request)   #相当于conn
        print('addr is: ',self.client_address) #相当于addr
        while True:
            try:
             data=self.request.recv(1024)
             if not data:
                 break
             print('收到的客户端消息是:',data)
             #发消息
             self.request.sendall(data.upper())

            except Exception as e:
                print(e)
                break

if __name__=='__main__':
    s=socketserver.ThreadingTCPServer(('192.168.0.101',8111),Myserver)
    print(s.RequestHandlerClass)
    print(Myserver)
    print(s.socket)
    print(s.server_address)
    s.serve_forever()

