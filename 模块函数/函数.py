############函数##################
#global
'''
name='xie'
def a():
    name='yang'
    print(name)
    global name#声明是全局变量的name,引用全局变量，并修改全局变量的值
    name='chuan'
a()
print(name)
'''
#nonlocal(也属于递归函数）
'''
name='123'
def a():
    name='456'
    print(name)
    def b():
        name='123'
        print(name)
        nonlocal name
        name='我是谁'

    b()
    print(name)
a()
'''
#递归函数（函数不能调用函数里面的里面的函数，只能调用子集函数）
'''
name='alex'
def foo():
    name='linhaifeng'
    def bar():
        name='wupeiqi'
        def c():
            global name
            name='test'
            print(name)
        print(name)
        c()
    print(name)
    bar()
foo()
print(name)
'''
#函数的作用域(return bar  没有括号只打印内存地址，函数没有return打印None)
'''
name='alex'
def foo():
    name='徐江南'
    def bar():
        name='谢传毅'
        print(name)
    return bar()
print(foo())
'''
#foo()()的使用
'''
def fool():
    test='XXX'
    print(test)
def foo():
    name='徐江南'
    def bar():
        name='谢传毅'
        print(name)
        return fool
    return bar()
print(foo()())
'''
#匿名函数（形参X数量不限）
#####lambda x:x+1相当于;
'''
def cal(x):
    return x+1
print(cal(2))
a=lambda x:x*x-2
print(a(4))
'''
#总结lambdade的使用如下：
'''
a=lambda x:x+'_test'
print(a('xjn'))
b=lambda x:x.capitalize()
print(b('computer'))
'''
##############函数式编程
##########函数式=编程语言定义的函数+数学意义的函数
'''
def foo():
    print('谢传毅')
    return foo
print(foo())
'''
#高阶函数：1.函数接收的参数是函数2、返回的值是函数
#尾调用优化（在函数的最后一步进入下一层递归（最后一步调用另外一个函数）
'''
def bar(n):
    return n+1
def foo(x):
    print('test hello world')
    return bar(x)
print(foo(1))
'''
###map函数#####
'''
#map可迭代对象
num_l=[1,3,4,5,7]
def map_test(array):
    ret=[]
    for i in array:
        ret.append(i**2)
    return ret
print(map_test(num_l))
'''
#map函数原理（1）
'''
num_l=[1,3,4,5,7]
def add_one(x):
    return x+1
def reduce_one(x):
    return x-1
def map_test(func,array):
    ret=[]
    for i in array:
        res=func(i)
        ret.append(res)
    return ret
print(map_test(add_one,num_l))
'''
#终极版本（2）
'''
num_l=[1,3,4,5,7]
def map_test(func,array):
    ret=[]
    for i in array:
        res=func(i)
        ret.append(res)
    return  ret
print(map_test(lambda x:x+1,num_l))
'''
#map函数的使用
'''
num_l=[1,23,4,5]
print(list(map(lambda x:x-2,num_l)))
'''
#过滤
'''#过滤原理
movie_people=["sb_test1","test","sb_manager","sb_product"]
ret=[]
for p in movie_people:
    if not p.startswith('sb'):#只能判断字符串
        ret.append(p)
print(ret)
'''
#filter函数实践
'''
movie_people=["sb_test1","test","sb_manager","sb_product",'test11']
def filter_test(array):
    ret=[]
    for p in array:
        if not p.startswith('sb'):
            ret.append(p)
    return ret
print(filter_test(movie_people))
'''
#终极版
'''
movie_people=['alex_sb','wupeiqi_sb','linhaifeng','yunhao_sb']
def sb_now(n):
    return n.endswith("sb")

def filter_test(func,array):
    ret=[]
    for p in array:''
        if not func(p):
            ret.append(p)
    return ret
print(filter_test(sb_now,movie_people))
'''
#filter函数
'''
movie_people=['alex_sb','wupeiqi_sb','linhaifeng','yunhao_sb']
print(list(filter(lambda n:not n.endswith('sb'),movie_people)))
'''
#reduce函数
'''
from functools import reduce#使用reduce函数，需引用reduce方法
num_l=[1,2,3,4,5,6,7]
res=0
for num in num_l:
    res+=num
print(res)
'''
#可迭代数字的总和
'''
def reduce_test(array):
    res=0
    for num in array:
        res+=num
    return res
#只允许列表，元组用该函数
a=[1,2,3,4,5,6,7]
b=(1,2,3,4,5,6,7)
c="1234567"
print(reduce_test(a))
'''
#2个参数的reduce函数
'''
num_l=[1,2,3,4,5,6,7]
def reduce_test(func,array):
    res=array.pop(0)#删除第一个值
    for num in array:
        res=func(res,num)
    return res
print(reduce_test(lambda x,y:x*y,num_l))
'''
#2、3个参数计算
'''
num_l=[1,2,3,100]
def reduce_test(func,array,init):
    if init is None:
        res=array.pop(0)
    else:
        res=init
    for num in array:
        res=func(res,num)
    return res
print(reduce_test(lambda x,y:x*y,num_l,100))
'''
#############内置函数############################
'''
#取绝对值abs()
print(abs(-5))
#判断所有值是否为真all()
print(all([1+1==2,1+3==4,'']))#可以判断计算的值
#只有一个值为真就是真any()
print(any([1+1==1,1+3==4]))
#将十进制转换二进制(ob)
print(bin(8))
#空，None，0的布尔值为False，其余为True
print(bool(''))
#字符串转换为字节(需要转字节码）
print(bytes('rest',encoding='utf-8'))
'''
name='你好'
'''
print(bytes(name,encoding='utf-8'))
#以什么编码
print(bytes(name,encoding='utf-8'))
#以什么解码
#print(name,deconde='utf-8')
#以gbk编码
print(bytes(name,encoding='gbk'))
#以gbk编码，以gbk解码
print(bytes(name,encoding='gbk',deconde='gbk'))
'''
'''
#chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
#####i -- 可以是10进制也可以是16进制的形式的数字。返回值是当前整数对应的ascii字符。
print(chr(97))
#dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
# 带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。
# 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
print(dir())
#10除以6，取商、余数
print(divmod(10,6))
'''
#字典转字符串
'''
dic={'name':'alex'}
dic_str=str(dic)
print(dic_str,type(dic_str))
#用来执行一个字符串表达式，并返回表达式的值。
print(eval(dic_str))
'''
'''
#hash() 用于获取取一个对象（字符串或者数值等）的哈希值。
print(hash(str([1,2,3])))
#帮助
help(all)
'''
'''
#10进制转2进制
print(bin(10))
#10进制转16进制
print(hex(12))
#10进制转8进制
print(oct(12))
'''
#判断1是否是字符串类型
'''
print(isinstance(1,str))
'''
#打印全局变量，包括系统提供的全局变量
'''
name='abcdefg'
print(globals())
print(_name_)
print(locals())
'''
#max.min函数
'''
l=[1,2,36,-1,80]
print(max(l))
print(min(l))
'''
#zip()要求：列表、元组、字符串
'''
print(tuple(zip(('a','b','c'),(1,2,3))))
'''
'''
a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b) # 返回一个对象
print(zipped)
print(ist(zipped)) # list() 转换为列表
print(list(zip(a,c)))              # 元素个数与最短的列表一致
a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
print(list(a1))
print(list(a2))
'''
#字典怎么用zip()
'''
p={'name':'alex','age':18,'gender':'none'}
print(list(zip(p.keys(),p.values())))
print(zip(p.keys(),p.values()))#内存地址
#max()、min()方法
'''
'''
age_dic={'age':18,'age1':13,'age4':10,'age3':20}
print(max(age_dic.values()))
print(max(age_dic.keys()))
print(max(age_dic))#默认比较的字典是key
'''
'''
age_dic={'age':18,'age1':13,'age4':10,'age3':20}
#判断最大的keys，输出最大的keys及对应的values。切换位置则判断最大的values
print(list(max(zip(age_dic.keys(),age_dic.values()))))
'''
'''
li=['a30','b2','c1']
print(max(li))#比较的是字符串里的第一个元素大小
'''
'''
#四舍五入
print(round(1.5))
#切片
l='hello'
s1=slice(2,5)
print(l[s1])
'''
