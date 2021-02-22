from time import *
#显示当前时间
print(localtime(time()))
#显示0时区的时间
print(gmtime())
#转换自定义的格式
print(strftime('%Y-%m-%d %X',localtime()))
# F相当于 %Y-%m-%d
print(strftime('%F %X',localtime()))
#显示星期、月。日。时间。年
print(ctime())

