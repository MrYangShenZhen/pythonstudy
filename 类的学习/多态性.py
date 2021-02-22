#子类和父类存在相同方法时，子类会覆盖父类方法
#运形时总会调用子类方法--> 多态


class Animal(object):
    def run(self):
        print('running...')
    def cry(self):
        print('crying...')

class Dog(Animal):
    def run(self):
        print('dog running...')

    def eat(self):
        print('dog eating...')

class Cat(Animal):
    def run(self):
        print('cat running...')

cat = Cat()
cat.run()

dog = Dog()
dog.run()

