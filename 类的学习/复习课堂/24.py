################类属性的增删改查#################
class School:
    Leader='老王'
    def __init__(self,name):
        self.name=name

    def Tescher(self):
        print("%s是新来的老师"%self.name)


print(School.Leader)#获取类的静态属性值

print(School.Tescher)#获取动态属性的内存地址

School.Leader='老杨'#修改类属性
School.Student="李同学"#类增加属性
print(School.Leader)

pl=School('小刘')
pl.Tescher()
pl.Student='王同学'#修改对象属性
print(School.__dict__)#查看类存在的属性
print(pl.__dict__)#查看对象存在的属性
del School.Leader#删除类属性
del pl.name#删除对象属性
print(School.__dict__)#查看类存在的属性
print(pl.__dict__)#查看对象存在的属性

'''实例对象如果没有该属性可以获取类的属性来使用，类没有再去找父类'''



