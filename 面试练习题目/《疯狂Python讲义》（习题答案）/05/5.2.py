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
def bubble_sort(list):
    list_len = len(list)
    for i in range(0, list_len):
        is_sorted = True
        for j in range(0, list_len - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                is_sorted = False
        if is_sorted: return
list1 = [3, 6, 1, 8, 5, -20, 100, 50, 200, -32, 123]
bubble_sort(list1)
print(list1)
