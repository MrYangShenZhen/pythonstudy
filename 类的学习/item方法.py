class Foo:#item与attr一样的效果，getitem取到值才会触发，没取到报错
    def __getitem__(self, item):
        print("get world")
        return self.__dict__[item]
    def __setitem__(self, key, value):
        print("hello world")
        self.__dict__[key]=value
    def __delitem__(self, key):
        print("del world")
        self.__dict__.pop(key)
s=Foo()
s.name="测试"
s['工具']='Jmeter'
print(s.__dict__)
del s.name   #删除中括号里的key会触发__delitem__
print(s.__dict__)
print(s['工具'])#获取中key会触发__delitem__
