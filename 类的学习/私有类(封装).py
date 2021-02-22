#####双下划线代表该属性是类的私有属性。只能内部调用

########　私有属性/方法可以在类本身中使用，但不能在类/对象外、子类/子类对象中使用python中的封装操作，
########  不是通过权限限制而是通过改名实现的可以通过“类名.__dict__”查看属性（包括私有属性）和值，在类的内部使用
########  私有属性，python内部会自动改名成“_类名__属性名”形式


class People(object):
    def __init__(self,name,age,gender, money):
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def __play(self):  
        print("王者荣耀正在进行时")

    def test(self):
    	self.__play()

p1 = People('user1', 10, 'male', 1000000)
print(p1.gender)
# print(p1.__money)
# p1.__play()
# p1.test()
p1.__play()
