########通过iter()内置函数取得可迭代对象的迭代器。

# list = [1,2,3,4,5]  # list是可迭代对象
# lterator = iter(list)  # 通过iter()方法取得list的迭代器
# print(lterator)
# ####next()函数是通过迭代器获取下一个位置的值。
# print(next(lterator))  # 1
# print(next(lterator))  # 2
# print(next(lterator))  # 3
# print(next(lterator))  # 4
# print(next(lterator))  # 5
# print(next(lterator))

#####判断一个对象是否可迭代isinstance(object,classinfo)内置函数可以判断一个对象是否是一个已知的类型，类似 type()
#####object -- 实例对象。
#####classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组

########需要知道collections模块里的Iterable。通俗点讲，凡是可迭代对象都是这个类的实例对象。
# import collections

# print(isinstance([1, 2, 3], collections.Iterable))
# print(isinstance((1,2,3), collections.Iterable))
# print(isinstance({"name":"chichung","age":23}, collections.Iterable))
# print(isinstance("sex", collections.Iterable))
# print(isinstance(123,collections.Iterable))
# print(isinstance(True,collections.Iterable))
# print(isinstance(1.23,collections.Iterable))


