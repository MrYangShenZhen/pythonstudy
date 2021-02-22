'''
#列表可以修改，直接追加不用赋值
li=[1,2,3,'we']
li.append('eddf')
print(li)
'''
'''
#计算列表存在元素的个数次数
li=['a',32,'eww']
v=li.count('a')
print(v)
'''
#字符串转列表
'''
a='12345'
b=list(a)
print(b)
'''
###########列表转字符串
#如果都是字符串
'''
li=['ada','sad',123,'fadtf']
s=""
for i in li:
    s = s + str(i)
print(s)
#如果都是字符串
li=['adada','adqeqr','afaf']
v = ''.join(li)
print(v)
'''
li=[11,22,33,44]
#列表追加数据
li.append({'add':123,'weq':213})
print(li)
#清空列表
li.clear()
print(li)