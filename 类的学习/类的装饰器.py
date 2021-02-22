# def desc(obj):
#     print("hello world")
#     # print(obj)
#     obj.a=1
#     obj.b=2
#     return obj
# @desc  #类的装饰器基本用法，@后函数，类都能做参数传入desc
# class Foo:
#     pass
# print(Foo.__dict__)
###############################修改版
# def Typed(**kwargs):
#     def dec(obj):
#         print(kwargs)
#         print(obj)
#         for key,value in kwargs.items():
#             setattr(obj,key,value)
#         return obj
#     print(kwargs)
#     return  dec
# @Typed(x=1,y=2,z=3)
# class Foo:
#     pass
# print(Foo.__dict__)
############################类的装饰器应用##################
class Type:
    def __init__(self,key,type):
        self.key=key
        self.type=type
    def __get__(self, instance, owner):
        print('这是get')
    def __set__(self, instance, value):#有set是数据描述符
        print('这是set')
        if not isinstance(value,self.type) :
            raise TypeError("类型错误,%s不是%s类型"%(self.key,self.type))
        instance.__dict__[self.key]=value
    def __delete__(self, instance):
        print('这是delete')
        print("instance参数是【%s】" %instance)
def Typed(**kwargs):
    def dec(obj):
        for key,value in kwargs.items():
            setattr(obj,key,Type(key,value))
        return obj
    return  dec
@Typed(name=str,age=int)
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s=Foo('alex',18)