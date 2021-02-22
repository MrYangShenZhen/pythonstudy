# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2020, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import socket, threading, CrazyitProtocol, os
from tkinter import simpledialog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import time

SERVER_PORT = 30000

class App:
    def __init__ (self, master):
        self.master = master
        self.init()
    def client_target(self, s):
        try:
            # 不断地从socket中读取数据，并将这些数据打印输出
            while True:
                line = self.s.recv(2048).decode('utf-8')
                if line is not None:
                    self.text.config(state=NORMAL)
                    self.text.insert(END, line + "\n")
                    self.text.config(state=DISABLED)
        # 使用finally块来关闭该线程对应的socket
        finally:
            self.s.close()
    def init (self):
        # ---------------------初始化界面-----------------------
        showf = Frame(self.master)
        showf.pack()
        self.text = Text(showf, width=80, border=1,
            height=30, font=('StSong', 14),
            foreground='gray')
        # 禁止编辑Text
        self.text.config(state=DISABLED)
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)
        # 创建Scrollbar组件，设置该组件与self.text的纵向滚动关联
        scroll = Scrollbar(showf, command=self.text.yview)
        scroll.pack(side=RIGHT, fill=Y)
        # 设置self.text的纵向滚动影响scroll滚动条
        self.text.configure(yscrollcommand=scroll.set)
        f = Frame(self.master)
        f.pack()
        self.entry = ttk.Entry(f, width=74,
            font=('StSong', 14),
            foreground='gray')
        self.entry.pack(side=LEFT, fill=BOTH, expand=YES)
        self.button = ttk.Button(f, text='发送')
        self.button.pack(side=RIGHT, fill=BOTH, expand=YES)
        # ---------------------初始化网络-----------------------
        # 创建socket对象
        self.s = socket.socket()
        try:
            # 连接远程主机
            self.s.connect(('192.168.1.88', SERVER_PORT))
            tip = ""
            # 采用循环不断地弹出对话框要求输入用户名
            while True:
                user_name = simpledialog.askstring('您的用户名', tip + '输入用户名:')
                # 在用户输入的用户名前后增加协议字符串后发送
                self.s.send((CrazyitProtocol.USER_ROUND + user_name
                    + CrazyitProtocol.USER_ROUND).encode('utf-8'))
                time.sleep(0.2)
                # 读取服务器端的响应
                result = self.s.recv(2048).decode('utf-8')
                if result is not None and result != '':
                    # 如果用户名重复，则开始下次循环
                    if result == CrazyitProtocol.NAME_REP:
                        tip = "用户名重复！请重新"
                        continue
                    # 如果服务器端返回登录成功，则结束循环
                    if result == CrazyitProtocol.LOGIN_SUCCESS:
                        break
        # 捕获到异常，关闭网络资源，并退出该程序
        except Exception as e:
            print("网络异常！请重新登录！", e)
            self.s.close()
            os._exit(1)
        self.button['command'] = self.send
        self.entry.bind('<Return>', self.entry_send)
        # 启动客户端线程
        threading.Thread(target=self.client_target, args=(self.s,)).start()
    def entry_send (self, e):
        self.send()
    def send (self):
        line = self.entry.get()
        if line is None or line == 'exit':
            return
        self.entry.delete(0, END)
        # 如果发送的信息中有冒号，且以//开头，则认为想发送私聊信息
        if ":" in line and line.startswith("//"):
            line = line[2:]
            self.s.send((CrazyitProtocol.PRIVATE_ROUND 
                + line.split(":")[0] + CrazyitProtocol.SPLIT_SIGN
                + line.split(":")[1] + CrazyitProtocol.PRIVATE_ROUND).encode('utf-8'))
        else:
            self.s.send((CrazyitProtocol.MSG_ROUND + line
                + CrazyitProtocol.MSG_ROUND).encode('utf-8'))
root = Tk()
root.title('聊天室')
App(root)
root.mainloop()
