# class school:
#     '我是赣州人'
#     def __init__(self,sheng,chenghu,techang):
#         self.local=sheng
#         self.name=chenghu
#         self.test=techang
#     def xisu(self):
#         return ('%s赣州人会搞灯笼'%self.local)
#     def xisu02(self):
#         return('%s赣州人会打米果'%self.local)
# d1=school('江西','老表','脐橙')
# print(d1.xisu())
# school.mingzi='共黑老板'#类的增加
# print(school.__dict__)
# del school.mingzi#类的删除
# print(school.__dict__)
# class school:
#     shiwu01='树木'
#     shiwu02='洗手间'
#     shiwu03='田径场'
#     def __init__(self,Name,Class,Paiming):
#         self.Name=Name
#         self.Class=Class
#         self.Paiming=Paiming
#     def yundong(self):
#         return('%s班%s名的%s在%s打篮球'%(self.Class,self.Paiming,self.Name,self.shiwu03))
#     @property#跟实例绑定
#     def clean(self):
#         return('hello python')
#     @classmethod#跟类绑定，实例也能拿
#     def reward(self):
#         return('hello world')
#     @staticmethod#不跟任何实例，类绑定
#     def fold():
#         return ('我是你大爷')
# p1=school('张杰','3','11')
# print(p1.__dict__)
# print(p1.shiwu01)
# print(p1.yundong())
# p2=school('李名','4','44')
# print(p2.clean)#跟实例绑定
# print(p2.reward())#跟类绑定，实例也能拿
# print(school.fold())#不跟任何实例，类绑定
# class school:
#     def __init__(self,name,addr):
#         self.name=name
#         self.addr=addr
# class Course:
#     def __init__(self,name,price,period,school):
#         self.name=name
#         self.price=price
#         self.period=period
#         self.school=school
#
# s1=school('old boy','北京')
# s2=school('old boy','南京')
# s3=school('old boy','东京')
# c1=Course('linux',10,'1h',s1)
# #同c1=Course('linux',10,'1h',s1.name)-print(c1.school)
# print(c1.school.name)
###########类的继承########
# class test01:
#     def a(self):
#         print('%s开发一下'%self.name)
#
# class test02(test01):
#     def __init__(self,name):
#         self.name=name
#     def b(self):
#         print('%s测试一下'%self.name)
# print(test02('开发').b())
######子类中调用父类
# class Vehicle:
#     def __init__(self,name,speed,load):
#         self.name=name
#         self.speed=speed
#         self.load=load
#     def run(self):
#        print('开动了')
# class Subway(Vehicle):
#     def __init__(self,name,speed,load,line):
#         # self.name=name
#         # self.speed=speed
#         # self.load=load
#         super().__init__(name,speed,load)
#         self.line=line
#     def run(self):
#         super().run()
#         print('载客%s的%s线地铁开动了'%(self.load,self.line))
# s1=Subway('北京交通',50,1000,13)
# s1.run()
# class Name:
#     mkname="ceshi"
#     def __init__(self,name):
#         self.name=name
#     def push(self):
#         pass
# b1=Name('xu')
# print(hasattr(Name,"mkname"))#只检查value
# print(hasattr(b1,"name"))#只检查value
# print(getattr(Name,'push'))#获取类数据属性的值，函数属性的内存地址
# print(getattr(b1,'name'))#获取对象
# setattr(b1,'sb1',123)#object,key,value,给对象加数据属性
# print(dir(b1))
# print(hasattr(b1,'sb1'))
# print(getattr(b1,'sb1'))
class temple:
    def __init__(self,name):
        self.name=name
    def __getattr__(self, item):#可以返回值,没有属性时触发
        return ('属性不对',item)
    def __delattr__(self, item):#不能返回值，删除时触发
        print("删除的属性是:",item)
    def __setattr__(self, key, value):#设置属性时触发
        print ("设置的属性是%s,值是%s"%(key,value))
p1=temple("小明")
# print(p1.name2)
# p1.name1=222
# del p1.name1
print(dir(p1))
# print(p1.name)
