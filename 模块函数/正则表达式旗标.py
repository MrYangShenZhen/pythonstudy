#re.A只匹配ASCII字符。可用(?a)代表
import re

# #re.I使用正则表达式匹配时不区分大小写
# #默认区分大小写
# print(re.findall(r'fkit','Fkit is a good domain,FKIT is good'))
# #使用re.I指定不区分大小写
# print(re.findall(r'fkit','Fkit is a good domain,FKIT is good',re.I))


#re.L使用正则表达式匹配时不区分大小写。只对bytes模式起作用。行内旗标(?L)

#re.M多行模式的旗标   
#"^"能匹配字符串的开头和每行的开头
#"$"能匹配字符串的末尾和每行的末尾
#默认情况下只"^" "$" 匹配字符串的开头


#re.S 让点(.)能匹配包括换行符在内的所有字符。
#如果不指定旗标则默认点(.)能匹配不包括换行符在内的所有字符


#re.X通过该旗标允许分行书写正则表达式，也允许为正则表达式添加注释
a=re.compile(r"""020 #广州的区号
			\-   #中间的短横线
			\d{8}  #8个值""",re.X)
b=re.compile(r'020\-\d{8}')