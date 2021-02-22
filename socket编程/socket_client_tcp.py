import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('192.168.0.101',8000))
# while True:
#     a=input("请输入称呼:")
#     if not a:continue
#     if a=='quit':break
#     phone.send(a.encode("utf-8"))
#     data=phone.recv(1024)
#     print('服务端收到消息是:',data.decode("gbk"))
# phone.close()