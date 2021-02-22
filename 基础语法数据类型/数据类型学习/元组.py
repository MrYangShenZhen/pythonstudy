#tuple不可修改，元素不可增加，删除
'''
tu=(1,2,3,4,)
#索引
v=tu[1]
print(v)
#切片
v=tu[0:2]
print(v)
#k可以被for循环
for item in tu:
    print(item)
    '''
'''
s='ahdiohaifoaof'
li=['adsa',123,'123rf']
tu=(123,'sder',[123,'er'],)
#字符串转元组
v=tuple(s)
#列表转元组
a=tuple(li)
#元组转列表
b=list(tu)
print(v,a,b)
'''
'''
#元组转字符串与列表转字符串一至
#有数字，有字符串
li=(11,22,33,'re',45,65)
s=''
for item in li:
    s=s+str(item)
print(s)
#只有字符串
li=['we','fsf']
v=''.join(li)
print(v)
'''
#def extend ()可迭代对象

#元组一级元素不可修改，但一级元素的列表可以修改
'''
#def count()获取指定元素在元组中出现的位置
li=('we','are','num',2,)
v=li.count('we')
print(v)
'''

#def index() 获取元素的索引位置(数字）
li=(1,2,3,4,5,'real',)
v=li.index('real')
print(v)

