class Type:
    def __init__(self,key,type):
        self.key=key
        self.type=type
    def __get__(self, instance, owner):
        print('这是get')
        # print("instance参数是【%s】" %instance)
        # print("owner参数是【%s】" %owner)
    def __set__(self, instance, value):#有set是数据描述符
        print('这是set')
        # print("instance参数是【%s】" %instance)
        # print("value参数是【%s】" %value)
        if not isinstance(value,self.type) :
            raise TypeError("类型错误,%s不是%s类型"%(self.key,self.type))
        instance.__dict__[self.key]=value
    def __delete__(self, instance):
        print('这是delete')
        print("instance参数是【%s】" %instance)
class People:
    name=Type('name',str)
    age=Type('age',int)
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
p1=People("测试",18,33.33)