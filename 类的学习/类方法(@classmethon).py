####如果不想通过实例来调用类的函数属性，而直接用类调用函数方法，则这就是类方法，通过内置装饰器@calssmethod
####类名.类方法()   类方法只是给类使用（无论是否存在实例），只能访问实例属性（变量）
####classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。


class cal:
    cal_name = '计算器'
    def __init__(self,x,y):
         self.x = x
         self.y = y
 
    @property           #在cal_add函数前加上@property，使得该函数可直接调用，封装起来
    def cal_add(self):
         return self.x + self.y
 
    @classmethod        #在cal_info函数前加上@classmethon，则该函数变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性
    def cal_info(cls):  #python自动传入位置参数cls就是类本身
         print('这是一个%s'%cls.cal_name)   #cls.cal_name调用类自己的数据属性
 
cal.cal_info()   #>>> '这是一个计算器'