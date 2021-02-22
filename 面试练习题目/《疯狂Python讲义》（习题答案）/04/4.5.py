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
lines = int(input("输入要打印的行数(奇数):"))
if lines % 2 == 0:
    print('请输入奇数')
    import sys
    sys.exit(0)
half_lines = lines // 2 + 1
# 打印上半
for i in range(half_lines):
    print(" " * (half_lines - i), end="")
    if i == 0:
        print("*")
    else:
        print("*", end="")
        print(" " * (2 * i - 1), end="")
        print("*")
# 打印下半
for i in range(half_lines - 1):
    print(" " * (i + 2), end="")
    if i == half_lines - 2:
        print("*")
    else:
        print("*", end="")
        print(" " * (lines - 4 - 2 * i), end="")
        print("*")
