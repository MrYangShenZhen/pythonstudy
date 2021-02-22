#十进制转换二进制
# print(bin(4))
#十进制转十六进制
# print(hex(15))
# print('{0}344{1}'.format('aa','bb'))
#三元运算，三目运算
# a=1
# b='test'if a==1else'objk'
# print(b)
#lambda表达式
# def count(arg):
#     return arg+1
# print(count(3))
# a=lambda arg:arg+1
# print(a(1))
#map
# li=[1,2,3,4,5]
# def func(s):
#     return s+1
# ret=map(func,li)
# print(list(ret))
#filter.遍历列表，去符合函数的返回值
# li=[22,33,44,55,66]
# def func(s):
#     if s>33:
#         return s
# ret=filter(func,li)
# print(list(ret))
# print(list(filter(lambda s:s>33,li )))
#reduce,列表元素相加得总和
from functools import  reduce
li=[1,2,3,4]
def func(a,b):
    return a+b
ret=reduce(func,li)
print(ret)