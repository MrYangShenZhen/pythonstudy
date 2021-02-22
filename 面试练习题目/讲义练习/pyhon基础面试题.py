#两个变量的交换
#1
# a=20
# b=30
# print(a,b)
# c=a
# a=b
# b=c
# print(a,b)
#2
# a,b=b,a
# print(a,b)
#3
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
#4位运算符的方式.什么是位运算符？



#有四个数:1,2,3,4，能组成多少个互不相同且无重复数字的三位数？各是多少?
# 排列组合传统方法
# sum = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i!=j) and (i!= k) and (j!=k):
#                 sum = sum+1
#                 print ('第%d组合是： %d%d%d.'%  (sum,i,j,k))
###itertools中的排列组合迭代器
import itertools
#长度r元组，所有可能的排列，无重复元素
# a=[int(''.join(x)) for x in itertools.permutations('1234',3)]
# print(a)
##笛卡尔积，相当于嵌套的for循环.所有组合结果
# b=[int(''.join(x)) for x in itertools.product('1234',repeat=3)]
# print(b,len(b))
# ##长度r元组，有序，无重复元素
# c=[int(''.join(x)) for x in itertools.combinations('1234',3)]
# print(c,len(c))
# # 长度r元组，有序，元素可重复
# d=[int(''.join(x)) for x in itertools.combinations_with_replacement('1234',3)]
# print(d,len(d))
