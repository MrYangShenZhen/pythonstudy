#####统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1,-9, -4, -5, 8]
##方法一
# a=[1, 3, 5, 7, 0, -1,-9, -4, -5, 8]
# b=0
# c=0
# for i in a:
#     if i >0:
#     	b+=1
#     if i <0:
#     	c+=1
# print('正数有%s'%b)
# print('负数有%s'%c)
##方法二
# a=[1, 3, 5, 7, 0, -1,-9, -4, -5, 8]
# b=[i for i in a if i >0]
# c=[i for i in a if i <0]
# print('正数有%s'%len(b))
# print('负数有%s'%len(c))



#####字符串 "axbyczdj"，如果得到结果“abcd”
##方法一  字符串切片
# a = "axbyczdj"
# print(a[::2])
##方法二
# a = "axbyczdj"
# c=[]
# for i in range(len(a)):
# 	if i % 2 == 0:
# 		c.append(a[i])
# print("".join(c))



#字符串切割
#####已知一个字符串为“hello_world_yoyo”, 如何得到一个队列["hello","world","yoyo"]
# a = "hello_world_yoyo"
# b = a.split("_")
# print(b)

#str.split(str="", num=string.count(str)).   分隔符、分隔次数


##格式化输出
#####已知一个数字为 1，如何输出“0001”
# a=1
# print("%04d"%a)



#####队列
####已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
# a = [1, 3, 5, 7]
# ##用insert插入数据
# a.insert(3,a[0])
# print(a[1:])



#####交换
####已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9
# a = 8
# b = 9

#方法1
#a,b=b,a

#方法二
# c=a
# a=b
# b=c

# print(a)
# print(b)





######印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
######其各位数字立方和等于该数本身。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋5 的三次方＋3 的三次方
# sxh=[]
# for i in range(100,1000):
# 	s=0
# 	m=list(str(i))
# 	for j in m:
# 		s+=int(j)**len(m)
# 	if s==i:
# 		print(i)
# 		sxh.append(i)
# print(sxh)






#####完全数
####如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备
####数。 例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余
####3 个数相加，1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28
####外，其余 5 个数相加，1+2+4+7+14=28。那么问题来了，求 1000 以内的完全数有哪些？
# a=[]
# for i in range(1,1000):
# 	s=0
# 	for j in range(1,i):
# 		if i % j== 0 and j<i:
# 			s+=j
# 	if s==i:
# 		print(i)
# 		a.append(i)
# print(a)




####列表倒叙
# a=[1, 3, 6, 9, 7, 3, 4, 6]
# # 1.sort 排序，正序
# a.sort()
# print(a)
# # 2.sort 倒叙
# a.sort(reverse=True)
# print(a)
# # 3.去重
# b = list(set(a))
# print(b)


####计算n的阶乘
####函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
####用传给 reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得
####到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
####计算 n!,例如 n=3(计算 3 2 1=6)， 求 10!
####方法一
# a=10
# s=1
# for i in range(1,a+1):
# 	s=i*s
# print(s)

####方法二
# from functools import reduce
# a=10
# b=reduce(lambda x,y:x*y,range(1,a+1))
# print(b)


####方法三递归
# def digui(num):
# 	if num==1:

# 		return 1
# 	else:
# 		return num*digui(num-1)
# a=10
# print(digui(10))


####斐波那契数列
# a = 0
# b = 1
# while b < 100:
# 	print(b, end=",")
# 	a, b = b, a+b




#幂的递归
####计算 x 的 n 次方，如：3 的 4 次方 为 3*3*3*3=81
# def mi(x, n):
# ####计算 x 的 的 n 次方
# 	if n == 0:
# 		return 1
# 	else:
# 		return x*mi(x, n-1)

# print(mi(3,5))



