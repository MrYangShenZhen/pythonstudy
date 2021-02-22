class Open:
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        print('执行enter')
        return self   #必须要有返回值才能用f去调用
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('执行exit')
        print(exc_type) #异常类
        print(exc_val)  #异常值
        print(exc_tb)   #追踪信息
        return True    #exit”吃“掉异常，继续执行块外的代码
# Foo=Open("a.txt")#不会执行enter,exit
with Open('b.txt') as f:
    print(f.name)
   # print(abc)
    print('hello')
print('测试一下')
