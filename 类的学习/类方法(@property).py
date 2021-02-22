###既要保护类的封装特性，又要让开发者可以使用“对象.属性”的方式操作操作类属性，除了使用 property() 函数，Python 还提供了 @property 装饰器。
###通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号。

class Rect:
    def __init__(self,area):
        self.__area = area
    @property
    # @area.setter   #有问题
    def area(self,value):
        self.__area=value
        return self.__area

rect = Rect(30)
#直接通过方法名来访问 area 方法
print("矩形的面积是：",rect.area)
###使用 ＠property 修饰了 area() 方法，这样就使得该方法变成了 area 属性的 getter 方法。需要注意的是，如果类中只包含该方法，那么 area 属性将是一个只读属性。

###也就是说，在使用 Rect 类时，无法对 area 属性重新赋值，即运行如下代码会报错：
# rect.area = 90
# print("修改后的面积：",rect.area)


#用@property装饰后，只有getter读的特性。还需要为 area 属性添加 setter 方法，就需要用到 setter 装饰器，它的语法格式如下：
#@方法名.setter
#def 方法名(self, value):
#    代码块
#