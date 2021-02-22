#列表顺序排序
# def group(list):
#     list.sort()
#     return list
#列表倒叙排序
# def gp(list):
#     list.sort()
#     list.reverse()
#     return list
# a=group([2,4,1,3,7,5,6])
# b=gp([2,4,1,3,7,5,6])
# print(a,b)
#计算乘方的函数
# def bow(base,exponent):
#     result=1
#     for i in range(1,exponent+1):
#         result *= base
#     return result
# print(bow(4,5))
# #函数名赋值给变量，该变量能用来调用函数
# a=bow
# print(a(3,2))

#########局部变量，全局变量###############
######locals,globals的使用
# a=13
# b='test'
# def test():
#     age=18
#     hours=24
#     print(locals())
#     print(locals()['age'])
# print(globals()['b'])
# test()
#########函数后面对name赋值的语句都是对全局变量赋值########
# name='alex'
# def test():
#     global name
#     print(name)
#     name='孙悟空'
# test()
# print(name)
###列表元组，字典((疯狂讲义64页）
# 1.
# a=input('请输入第1个字符串：')
# b=input('请输入第2个字符串：')
# c=input('请输入第3个字符串：')
# d=a+b+c
# e=tuple(d)
# print(e*3)
# f=e+('fkjava','crazyit')
# print(f)
# 2.
# a=['apr','是你',2,'opp']
# b=['desk']
# for i in a:
#     b.append(i)
# print(b)
# 2.
# a=input('请输入一个整数:')
# b=[]
# for i in range(1,int(a)+1):
#     b.append(i)
# print(b)
# 3.
a=input('请输入一个整数:')
b=[]
for i in range(1,int(a)+1):
      if  not i/2==0:
          b.append(i)
          if  len(b) == int(a):
            print(b)