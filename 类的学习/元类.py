# class Foo:
#     pass
# # s1=Foo()
# # print(type(s1))
# # print(type(Foo))
# def __init__(self,name,age):
#     self.name=name
#     self.age=age
# def test(self):
#     print('nihao')
# FF=type('FF',(object,),{'age':12,'__init__':__init__,'test':test})#,代表元组，可继承多个类
# print(Foo.__dict__)
# print(FF.__dict__)
# f1=FF('lin',18)
# print(f1.name)
# print(f1.age)
# f1.test()
###################自定义元类
class Mytype(type):
    def __init__(self,a,b,c):
        print('这是元类')
        # print(a)
        # print(b)
        # print(c)
    def __call__(self, *args, **kwargs):
        print('运行call')
        print( *args, **kwargs)
        obj=object.__new__(self)#创建一个新的对象=>a
        self.__init__(obj,*args, **kwargs)#self是Foo
        return obj
class Foo(metaclass=Mytype):#Mytype(4个参数)=(self,'Foo',(object,),{属性字典})=>__init__
        def __init__(self,name):
            self.name=name
a=Foo('test')
print(a.__dict__)
