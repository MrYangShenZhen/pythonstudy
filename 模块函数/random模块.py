import random as rd
# print(rd.random())#打印随机0-1的浮点数（小数）
# print(rd.randint(1,3))#打印1-3的随机整数
# ret=rd.randrange(1,3)#
# ret=rd.choice([11,22,33])#选择11,22,33随机一个数
# ret=rd.sample([11,22,33,44,55],2)#随机取两个数
# ret=rd.uniform(1,3)#1-3之间的任意浮点数
# print(ret)
# reh=[1,2,3,4,5]
# print(rd.shuffle(reh)#打乱显示
######################sys模块##########r
import sys
# sys.path.append()#临时添加环境变量
# print(sys.path)#返回模块的搜索路径集（list)
# sys.exit()# 不执行下一行代码
# print('hello word')
print(sys.argv[0])#当前代码执行路径
command=sys.argv[1]
path=sys.argv[2]

if command=="post":
     pass

elif command=="get":
     pass

import time
for i in range(100):
    sys.stdout.write("#")
    time.sleep(0.1)
    sys.stdout.flush()
