#使用while循环输入 1 2 3 4 5 6  8 9 10
'''
a=0
while a<10:
    a=a+1
    if a!=7:
        print(a)
print('结束')
'''
#1-100所有数的和
'''
number=0
zong=0
while number<101:
    zong=zong+number
    number=number+1
print(zong)
'''
#1-100内的所有奇数
'''
num=1
while num<101:
    a=num%2
    if a==1:
        print(num)
    num=num+1
print('结束')
'''
#1-100内的所有偶数
'''
num=1
while num<101:
    a=num%2
    if a==0:
        print(num)
    num=num+1
print('结束')
'''
#求1-2+3-4+5-6+7-8+...99的所有数的和（1）
'''
a=1
b=2
d=0
while b<100:
    c=a-b
    a=a+2
    b=b+2
    d=c+d
e=d+99
print(e)
'''
#求1-2+3-4+5-6+7-8+...99的所有数的和（2）
'''
n=1
s=0
while n<100:
    a=n%2
    if a==0:
        s=s-n
    else:
        s=s+n
    n=n+1
print(s)
'''
#用户登录三次机会重试
'''
times=1
while times<4:
    a=input('请输入账号：')
    b=input('请输入密码：')
    if a=='15634859231'and b=='888888ywd':
        print('登录成功')
        break
    else:
        print('登录失败')
    times=times+1
if times==1:
    pass
else:
    print('你的登录次数已用完')
    '''
#练习
'''
test = "username\tpasswd\temail\nyangweidong\t888888ywd\t2011726042@qq.com\nyangweidong\t888888ywd\t2011726042@qq.com"
v = test.expandtabs(20)
print(v,len(v))
'''
#将字符串转换为数字
'''
a='123'
b = int(a)
c=b+7
print(c)
'''
#进制位数前面的0省略(输入多少进制转换为10进制表示）
'''
num='01000000'
v=int(num,base=2)
print(v)
'''
#输入数字来转换为二进制用几位来表示
'''
age=25
v=age.bit_length()
print(v)
'''
'''
test='SKW'
#如过首位字符是字母变为大写(其余字母都会变为小写）
v=test.capitalize()
print(v)
#如过字符是字母变为小写
v1=test.casefold()
print(v1)
v2=test.lower()
print(v2)
#设置空白或填充字符(只能填充一个字符)
v3=test.center(20,' ')
print(v3)
'''
'''
test='alex'
#判断以什么字母开头(区分大小写)
v=test.startswith('a')
print(v)
#判断以什么字母结尾(区分大小写）
v1=test.endswith('x')
print(v1)
'''
#从开始往后找，找到第一个获取其位置
'''
test='alexalex'
v=test.find('x',5,8)
print(v)
'''
#格式化，将一个字符串中的占位符（左开右闭）替换为指定的值
'''
test='i am {name},age {a}'
print(test)
v=test.format(name='alex',a=19)
v1=test.format_map({"name":'faker',"a":21})
print(v,v1)
'''
#格式化的另一种方法
'''
test='i am {0},age {1}'
print(test)
v1=test.format('alsdk',12)
print(v1)
'''
#字符串中是否只包含字母、数字和汉字
'''
test="阿迪adad"
v=test.isalnum()
print(v)
'''
#判断是否只包含字母、汉字
'''
test="我asad"
v=test.isalpha()
print(v)
'''
#判断是否是数字
'''
test="③"
#判断是否是10进制的整数
v=test.isdecimal()
#更强大的判断数字(特殊数字)
v1=test.isdigit()
print(v,v1)
'''
#判断字母、数字、下划线（数字是否开头）是否是标识符
'''
a = "我是"
v=a.isidentifier()
print(v)
'''
'''
test=" "
#判断字符串包含的字母是否都是小写
v=test.islower()
#判断字符串包含的是否都是数字(支持中文数字识别判断)
v1=test.isnumeric()
#判断字符串是否存在不可显示的字符，如：\t，\n
v2=test.isprintable()
#判断字符串是否全部都是空格
v3=test.isspace()
print(v,v1,v2,v3)
'''
'''
test="Process finished with exit code 0"
#判断是否是标题（每个单词首字母大写）
v=test.istitle()
#将字符串每个单词首字母转换为大写（即转换为标题）
v1=test.title()
print(v,v1)
'''
#字符串的每个元素按照指定分隔符进行拼接（很重要）
'''
test="我是风儿你是沙"
print(test)
t='a'
v=t.join(test)
print(v)
'''
'''
#右填充(内容放左边）
test="xiaoming"
v=test.ljust(20,'$')
print(v)
#左填充(内容放右边）
v1=test.rjust(20,'$')
print(v1)
#默认只用00左填充
v2=test.zfill(20)
print(v2)
'''
#判断是否全部大写或全部转换为大写
'''
test='alex'
v1=test.isupper()
v2=test.upper()
print(v1,v2)
'''
'''
test='eaudhaiu'
#去除左边空格(换行）(括号加内容去掉指定内容）
v=test.lstrip('de')
print(v)
#去除右边空格(括号加内容，去掉指定内容)
v1=test.rstrip()
print(v1)
#去除两边空格
v2=test.strip()
print(v2)

'''
#字符串中的a、e、i、o、u被1、2、3、4、5替换
'''
v='agfgausadadafafxzeytioadi,shacxs'
m=str.maketrans('aeiou','12345')
rv=v.translate(m)
print(rv)
'''
'''
test='tesabdiaidahdi'
#以‘s'进行分割成3份显示(从左开始定位s)
v=test.partition('s')
#以‘a'进行分割成3份显示(从右开始定位s)
v1=test.rpartition('a')
#以‘a'进行分割2个（从左开始定位，不输入数字分割所有）
v3=test.split('a',2)
#以‘a'进行分割2个（从右开始定位，不输入数字分割所有）
v4=test.rsplit('a',2)
print(v,v1,v3,v4)
'''
'''
#splitlines()不输入内容只根据换行符\n进行分割(输入True分割显示换行符\n,False不显示）
test='adhga\ndhgauif\tgiuf'
v=test.splitlines(False)
print(v)
'''
'''
test='bakfaioa'
#判断是否以a开头
v=test.startswith('a')
#判断是否以a结尾
v1=test.endswith('a')
print(v,v1)
'''
'''
#大小写切换（大写变小写，小写变大写）
test='asGgGiO'
v=test.swapcase()
print(v)
'''
###############以下内容其它数据类型能用########################
#索引下标获取字符串中的某一个字符
'''
test='alex'
v=test[2]
print(v)
'''
'''
#切片0<= [] <1
test='alex'
#获取字符串由几个数字组成
v1=len(test)
print(v,v1)
'''
'''
#for循环
test='wqredafqw212'
for i in test:
    print(i)
'''
'''
test='alexalexalex'
#替换字符串中的ex
v=test.replace("ex",'bb')
#替换字符串中前两个ex
v1=test.replace("ex",'bb',2)
print(v,v1)
'''
#获取连续的数字（后加数字可设置不连续）
'''
v=range(0,100,5)
for item in v:
    print(item)
    '''
#############七个必须掌握字符串知识#########
#join，split，find,strip,upper,lower,replace
##############基础作业#####################
#列表拼接
'''
v1="_".join('adahoifjoiajfoiajf')
#字符串拼接
v2="_".join(['sdad','213','daad'])
print(v1,v2)
'''
#实现一个整数加法计算
'''
value=input('请输入内容:')
v1,v2=value.split('+')
v3=int(v1)+int(v2)
print(v3)
'''
'''
#计算用户输入的内容有几个数字、几个字母
c1=0
c2=0
val=input('请输入内容：')
for item in val:
    if item.isdecimal() == True:
        c1 += 1
    else:
        c2 += 1
print(c1,c2)
'''
'''
#等待用户输入名字、地点、爱好
template='敬爱可爱的{0},最喜欢在{1}地方干{2}'
test1=input("名字：")
test2=input("地点：")
test3=input("爱好：")
v=template.format(test1,test2,test3)
print(v)
'''
'''
#制作随机验证码，并输入验证码判断是否输入正确
def check_code():
    import random
    check_code = ''
    for i in range(4):
        current = random.randrange(0,4)
        if current != i:
            temp =chr(random.randint(65,90))
        else:
            temp =random.randint(0,9)
        check_code += str(temp)
    return check_code
while True:
    code = check_code()
    print(code)
    v = input('>>>')
    v1 = v.lower()
    vcode = code.lower()
    if vcode == v1 :
        v3 = '》》回答正确'
        print(v,v3)
    else :
        print('输入错误')
'''
#过滤敏感字符
'''
a=input('请输入内容：')
a=a.replace('东京热','***')
a=a.replace('苍井空','***')
print(a)
'''
'''
#制作表格 循环提示用户输入：用户名、密码、邮箱
s = ''
times = 0
while times < 4:
    v1 = input('用户名：')
    v2 = input('密码：')
    v3 = input('邮箱：')
    template = '{0}\t{1}\t{2}\n'
    v = template.format(v1,v2,v3)
    s = s+v
    times +=1
print(s.expandtabs(20))
'''