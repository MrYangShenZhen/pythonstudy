import re
# ret=re.findall('\d+','agdgadg12131uidhduidhi`2')#匹配数字
# ret=re.findall('.','agdgadg12131uidhduidhi`2\n')#代表任意字符，除换行符
# ret=re.findall('^ag','agdgadg12131uidhduidhi`2\n')#^放在开头，以开头匹配内容，字符串开头没有则为空
# ret=re.findall('2$','agdgadg12131uidhduidhi`22')#$以2结尾匹配内容.结尾是2就输出2，没有就输出空元组
#ret=re.findall('d*','agdgaddg12131uidddhduidhi`2')#按紧挨着的字符重复，重复次数不限制(贪狼匹配，匹配前面那个字符)
# 重复的打印，没重复的打印空字符d*
#ret01=re.findall('d+','agdgaddg12131uidddhduidhi`2')#紧挨着的字符重复1-无穷次
#ret02=re.findall('d?','agdgaddg12131uidddhduidhi`2')#按紧挨着的字符重复，重复0次或1次(惰性匹配，匹配前面那个字符）
# print(ret)
# print(ret01)
# print(ret02)
# rea=re.findall('a{0,}','Aashdahhuhfiqhaahhdaaawww')#紧挨着的字符重复0-无穷次,相当于*
# rea=re.findall('a{1,}','Aashdahhuhfiqhaahhdaaawww')#紧挨着的字符重复0-无穷次,相当于+
# rea=re.findall('a{0,1}','Aashdahhuhfiqhaahhdaaawww')#紧挨着的字符重复0-1次,相当于？
# rea=re.findall('h{2}','Aashdahh1huhhfiqhaahhdaaawww')#匹配两次(找到两个紧挨着的h，并打印)
# print(rea)
# rea=re.findall('a{2,4}','Aaashdahhahuhfiqhaaahhdaaaawww')#匹配2-4任意次数
# rea=re.findall('ah*?','Aaashdahhahuhfiqhaaahhdaaaawww')#匹配*、?交集最小(重复0次)
# print(rea)
##########元字符之字符集[]#####
##管道符|是或的作用   #字符集里面没有特殊符号除-、^、\
reb=re.findall('www[oldboy baidu]','wwwbaidu')
# reb=re.findall('q[a-z]','q22wwsdas')#匹配一个任一a-z的字母，“^”表示非
# reb=re.findall('w\d+','w21dadddswwww')#\d+匹配至少一个数字
# reb=re.findall('w\D+','wd21dadddswwdww')#\D+匹配至少一个非数字
# reb=re.findall('w\s+','w  d21dadddsww  d  ww')#\s+匹配至少一个空字符
# reb=re.findall('w\S+','w  d21dadddsww  d  ww')#\S+匹配至少一个非空字符
# reb=re.findall('w\w+','w*b2d21dadddsw*2w  d  w4wf')#\w匹配任意字母、数字字符
# reb=re.findall('w\W+','w*b2d21dadddsw*2w  d  w4wf')#\W匹配任意非字母、数字字符
# reb=re.findall(r'w\b','w*b2d21dadddsw*2w  d  w4wf')#匹配特殊字符或边界
# reb=re.findall('c\\\\l','abc\lerwf')
# reb=re.findall(r'c\\\\l','abc\lerwf')
print(reb)
#######################
rec=re.search('a','alvin yuan').group()#只找到第一个匹配就返回一个包
# rec=re.match('a','alvin yuan').group()#字符串开始处进行查找匹配
# rec=re.split('[ab]','abcd')#先按a分割得到''和'bcd',再对''和'bcd'按'分割'
# rec=re.sub('\d+','c','sss2hu233er45s0')#替换字符串里的数字为c
# rec=re.sub('\d+','c','sss2hu233er45s0',2)#替换字符串里前2个数字为c
# rec=re.subn('\d+','c','sss2hu233er45s0')#替换并统计匹配的次数
# com=re.compile('\d+')
# rec=com.findall('sss2hu233er45s0')
print(rec)
##################################
# tet=re.finditer('\d','sdfg123dkflsia10w03s1')
# red=next(tet).group()
# print(tet)#返回的是迭代器对象
# print(red)#一个一个拿数字（从迭代器拿）
# ref=re.findall("www\.(?:baidu|163)\.com","https\\:www.baidu.com")#管道符号或的关系，?:去除只打印括号内容的优先级，打印所有
# print(ref)

########re.split#########
##re.split(pattern,string,maxsplit=0,flags=0):使用pattern对string进行分割，该函数返回分割得到的多个子串组成的列表
###其中maxsplit参数控制最多分割几次