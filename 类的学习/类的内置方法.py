#######改变对象的字符串显示
###单个str方法
# class Foo:#定制__str__方法，print时触发
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '录入用户姓名:%s,年龄：%s'%(self.name,self.age)
# s=Foo('大佬',24)
# print(s)
# print(str(s))
# print(s.__str__())
###单个repr方法
# class Foo:#定制__repr__方法，print时触发，用户解释器返回
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __repr__(self):#单独定制repr方法，print会触发repr方法
#         return '录入用户姓名:%s,年龄：%s'%(self.name,self.age)
# s=Foo('测试佬',24)
# print(s)
# print(repr(s))
# print(s.__repr__())
###存在repr,str方法
# class Foo:#定制__str__方法，print时触发
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '录入用户姓名:%s,年龄：%s'%(self.name,self.age)
#     def __repr__(self):#单独定制repr方法，print会触发repr方法
#         return '你好,%s'%self.name
# s=Foo('测试佬',24)
# print(s)#直接输出默认使用__str__
# print(repr(s))#可以调用repe
# print(s.__repr__())
########format方法
# x='{0}{0}{0}'.format('dog')#初始化字符串
# print(x)
# class Date:
#     def __init__(self,year,mon,day):
#         self.year=year
#         self.mon=mon
#         self.day=day
# d1=Date(2016,12,26)
# ##传入对象并调用对象的属性
# x='{0.year}{0.mon}{0.day}'.format(d1)
# y='{0.year}:{0.mon}:{0.day}'.format(d1)
# z='{0.mon}-{0.day}-{0.year}'.format(d1)
# print(x)
# print(y)
# print(z)
# format_dic={
#     'ymd':'{0.year}{0.mon}{0.day}',
#     'm-d-y':'{0.mon}-{0.day}-{0.year}',
#     'y:m:d':'{0.year}:{0.mon}:{0.day}'
# }
# class Date:
#     def __init__(self,year,mon,day):
#         self.year=year
#         self.mon=mon
#         self.day=day
#     def __format__(self, format_spec):
#         # print('我执行啦')
#         # print('--->',format_spec)
#         if not format_spec or format_spec not in format_dic:
#             format_spec='ymd'
#         fm=format_dic[format_spec]
#         return fm.format(self)
# d1=Date(2016,12,26)
# # format(d1) #d1.__format__()
# print(format(d1))
# print(format(d1,'ymd'))
# print(format(d1,'y:m:d'))
# print(format(d1,'m-d-y'))
# print(format(d1,'m-d:y'))
# print('===========>',format(d1,'asdfasdfsadfasdfasdfasdfasdfasdfasdfasdfasdfasdfasd'))
########__slots__方法
# class Foo:
#     __slots__=['name','phone']#定义属性的key，存在slots方法无法访问该类的__dict__
# s1=Foo()
# print(s1.__slots__)
# s1.name='测试'
# s1.phone='15634859231'
# print(s1.name)
# print(s1.phone)
# s2=Foo()
# print(s2.__slots__)
# s2.name='开发'
# s2.phone='15634859232'
# print(s2.name)
# print(s2.phone)
####__doc__方法,无法被子类继承
# class Foo:
#     '莫云还不发工资'
#     pass
# class Loo(Foo):
#     pass
# s1=Foo()
# s2=Loo()
# print(s1.__doc__,Foo.__dict__)
# print(s2.__doc__,Loo.__dict__)
####__module__,__class__方法
# from opj.module01 import Too
# s1=Too('test')
# print(s1.__module__)
# print(s1.__class__)
#########__del__
# class Foo:#删除对象或执行完py文件触发。删除属性不触发
#     def __init__(self,name):
#         self.name=name
#     def __del__(self):
#         print("正在清空")
# s1=Foo('测试')
# del s1.name
#############__call__
# class Foo:8
#     def __call__(self, *args, **kwargs):
#         print('执行call了')
# f1=Foo()
# f1()#对象执行Foo类下的__call__
# Foo()#对象执行**类下的__call__
########迭代器协议
# class Foo:#协议规定需要定义iter方法，next方法只能往后
#     def __init__(self,n):
#         self.n=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n == 15:
#             raise StopIteration('数量超标')
#         self.n+=1
#         return self.n
# s1=Foo(10)
# # print(s1.__next__())
# # print(next(s1))
# for i in s1:
#     print(i)
####斐波那契数列数列，如1,1,2,3,5,8,13...
class Foo():
    def __init__(self):
        self.a=1
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a > 100:
            raise StopIteration('结束')
        self.a,self.b=self.b,self.a+self.b
        return  self.a
s1=Foo()
print(s1.__next__())
print(s1.__next__())#执行for循环时不会重新去遍历
for i in s1:#for循环不会抛出异常提示，但会终止，不断print会抛出异常提示
    print(i)#最后输出会输出b