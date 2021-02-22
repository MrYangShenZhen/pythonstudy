class laProperty:
    def __init__(self,func):
        # print(func)
        self.func=func
    def __get__(self, instance, owner):
        # print(instance)
        # print(owner)
         if instance is None:
            return self
         res=self.func(instance)#执行area(self）
         setattr(instance,self.func.__name__,res)#将返回值加到实例对象属性字典里
         return res
class room:
    def __init__(self,name,length,width):
        self.name=name
        self.length=length
        self.width=width
    @laProperty #====area=laProperty(area)装饰器是类不用参数
    def area(self):
        return self.length*self.width
    @property
    def test(self):
        return ('12323444')
    # print(area.func)
r1=room('厕所',1,2)
print(r1.area)
print(r1.__dict__)
# print(room.test)
# print(room.area)


