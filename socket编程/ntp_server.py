from socket import  *
import time
server_port=("192.168.0.102",9001)
buffersize=1024
udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(server_port)
while True:
    data,addr=udp_server.recvfrom(buffersize)
    if not data:
        ftm=time.strftime("%y-%m-%d %X")
    if data:
        ftm=data.decode("utf-8")
    # print(data.decode("utf-8"))
    # print("客户端地址是:",addr)
    udp_server.sendto(ftm.encode("utf-8"),addr)