from socket import *
Server_IP=('192.168.0.101',8000)
phone=socket(AF_INET,SOCK_STREAM)
#phone.setsockopt(SOL_SOCKET,SO_REUSEADDR)#出现地址被使用时，使用该语句
phone.bind(Server_IP)
phone.listen(5)
while True:
    print('开始接受客户端连接')
    conn,addr=phone.accept()
    print("双向链接:",conn)
    print("客户端地址:",addr)
    while True:         #linux系统不能用try except去找寻异常，需if not msg:break如果不存在取值，跳出循环
        try:
         msg=conn.recv(1024)
         print('收到客户端消息:',msg.decode("utf-8"))
         conn.send("你好".encode('utf-8'))
        except Exception:
            break
conn.close()
phone.close()