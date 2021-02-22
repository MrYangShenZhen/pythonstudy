from socket import  *
server_port=("192.168.0.102",9001)
buffersize=1024
udp_server=socket(AF_INET,SOCK_DGRAM)
while True:
    msg=input("请输入内容:").strip()
    udp_server.sendto(msg.encode("utf-8"),server_port)
    data,addr=udp_server.recvfrom(buffersize)
    print(data)