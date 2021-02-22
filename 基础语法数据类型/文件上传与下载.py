#coding: utf-8
from ftplib import FTP
import time
import tarfile
#!/usr/bin/python
#-*- coding: utf-8 -*-

from ftplib import FTP

def ftpconnect(host, username, password):
    ftp = FTP()
    #ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, 21)          #连接
    ftp.login(username, password)  #登录，如果匿名登录则用空串代替即可
    print(ftp.dir())
    return ftp
    
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024                #设置缓冲块大小
    fp = open(localpath,'wb')     #以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize) #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)         #关闭调试
    fp.close()                    #关闭文件

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR '+ remotepath , fp, bufsize) #上传文件
    ftp.set_debuglevel(0)
    print('success')
    fp.close()                                    


if __name__ == "__main__":
    ftp = ftpconnect("qxu1587790024.my3w.com", "qxu1587790024", "MWTHxw2020")
    # downloadfile(ftp, "***", "***")
    # uploadfile(ftp, "timg.jpg", "E:/picture")
    ftp.quit()