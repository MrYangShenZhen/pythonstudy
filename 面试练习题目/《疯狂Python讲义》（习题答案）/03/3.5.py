# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com 公众号: fkbooks                  #
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
import random

length = int(input("请输入列表的长度:"))
my_list = []
for i in range(length):
    # 获得一个随机数
    num = random.randint(65, 65 + 25)
    my_list.append(chr(num))
print(my_list)
my_list = [chr(random.randint(65, 65 + 25)) for i in range(length)]
print(my_list)
