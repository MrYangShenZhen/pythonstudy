'''
#字符串拼接
print('i am %s my hobby is alex'%'lhf')
#字符串可接多个%拼接
print('i am %s my hobby is %s'%('lhf','alex'))
'''
#打印浮点数float(打印小数点后六位，四舍五入）
'''
tpl='percent %2f'%99.97623455
print(tpl)
#插入:
print('root','x','o','o',sep=':')
'''
#format(可索引取值，可重复使用）
'''
tpl="i am {},age{},{}".format("seven",18,"alex")
print(tpl)
tpl="i am {2},age{1},{0}".format("seven",18,"alex")
print(tpl)
tpl="i am {1},age{1}".format("seven",18,"alex")
print(tpl)
'''
##传字典
'''
tpl="i am {name},age{age},really{name}".format(name="seven",age=18)
print(tpl)
tpl="i am {name},age{age},really{name}".format(**{"name":"seven","age":18})
print(tpl)
'''
#传列表
# tpl="i am {:s},age{:d}".format("seven",18)
# print(tpl)
#切片
text="sssdwqw"
v=text[-2:]
print(v)