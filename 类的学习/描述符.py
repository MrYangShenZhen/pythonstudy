###############描述符理论
# class Foo:
#     def __get__(self, instance, owner):
#         print('这是get')
#     def __set__(self, instance, value):
#         print('这是set',instance,value)
#         instance.__dict__['bo']=value
#     def __delete__(self, instance):
#         print('这是delete')
# s1=Foo()
# print(s1.a)
# Foo.b=2
# print(s1.b)
# print(dir(s1))
# class Aut:
#     bo=Foo()#属性值又是描述符存在的类时
#     def __init__(self,n):
#         self.bo=n         #与属性同名称，会触发描述符类set的运行
# s2=Aut(10)
# print(s2.__dict__)
# s2.bo=1111111
# print(s2.__dict__)
# s2.bo#调用属性时触发get,属性值又是描述符存在的类时
# # print(s2.bo)
# s2.bo=2
# print(dir(s2))
# del s2.bo
#################验证优先级
###类属性>>>数据描述符>>>实例属性>>>非数据描述符>>>找不到属性
##############非数据描述符即不存在set
# class Foo:
#     def __get__(self, instance, owner):
#         print('这个是get')
#     def __set__(self, instance, value):
#         print('这个是set')
#     def __delete__(self, instance):
#         print('这个是delete')
# class Br:
#     x=Foo()
# s1=Br()
# # Br.x=1
# s1.x=1
# print(Br.__dict__)
# print(Br.x)
##################描述符牛刀小试###########
class Lazyproperty:
    def __init__(self,func):
        self.func=func
    def __get__(self, instance, owner):
        print('这是我们自己定制的静态属性,r1.area实际是要执行r1.area()')
        if instance is None:
            return self
        return self.func(instance) #此时你应该明白,到底是谁在为你做自动传递self的事情

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    @Lazyproperty #area=Lazyproperty(area) 相当于定义了一个类属性,即描述符
    def area(self):
        return self.width * self.length

r1=Room('alex',1,1)
print(r1.area)