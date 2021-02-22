from socket import  *
server_port=("192.168.0.101",8000)
buffersize=1024
udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(server_port)
while True:
    data,addr=udp_server.recvfrom(buffersize)
    print(data.decode("utf-8"))
    print("客户端地址是:",addr)
    udp_server.sendto(data.upper(),addr)