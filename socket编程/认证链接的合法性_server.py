#_*_coding:utf-8_*_
__author__ = 'Linhaifeng'
from socket import *
import hmac,os

secret_key=b'linhaifeng bang bang bang'
def conn_auth(conn):
    '''
    认证客户端链接
    :param conn:
    :return:
    '''
    print('开始验证新链接的合法性')
    msg=os.urandom(32)#是一种bytes类型的随机生成n个字节字符串的方法，而且每次生成的值都不相同。
    print(msg)
    conn.sendall(msg)
    h=hmac.new(secret_key,msg)
    print(h)
    digest=h.digest()
    print(digest)
    respone=conn.recv(len(digest))
    print(respone)
    return hmac.compare_digest(respone,digest)#比较两个密文是否一致

def data_handler(conn,bufsize=1024):
    if not conn_auth(conn):
        print('该链接不合法,关闭')
        conn.close()
        return
    print('链接合法,开始通信')
    while True:
        data=conn.recv(bufsize)
        if not data:break
        conn.sendall(data.upper())

def server_handler(ip_port,bufsize,backlog=5):
    '''
    只处理链接
    :param ip_port:
    :return:
    '''
    tcp_socket_server=socket(AF_INET,SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn,addr=tcp_socket_server.accept()
        print('新连接[%s:%s]' %(addr[0],addr[1]))
        data_handler(conn,bufsize)

if __name__ == '__main__':
    ip_port=('192.168.0.101',9999)
    bufsize=1024
    server_handler(ip_port,bufsize)
