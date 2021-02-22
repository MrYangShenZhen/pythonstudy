import re
##在匹配的字符串前后添加内容
def fun(matched):
	#matched就是匹配对象，通过该对象的group方法客户区被匹配的字符串
	value="《疯狂"+(matched.group('lang'))+"讲义》"
	return value

s='python很好,kotlin也很好'
#对s立面的英文单词(用re.A旗标控制)进行替换
#使用fun函数指定替换的内容
print(re.sub(r'(?P<lang>\w+)',fun,s,flags=re.A))
