#####文件处理######
# f=open('F:\Py3.5\quanzhang_study\字典.py',encoding='utf-8')
# data=f.read()
# 是否可读
# print(f.readable())
#读一行
# print(f.readline())
# 所有行放到列表里
# data=f.readlines()
# print(data)
# f.close()
# f=open('F:\Py3.5\quanzhang_study\ojbk.txt','w',encoding='utf-8')
# 内容写进文件去
# f.write('我爱你\n知道吗？')
#判断是否可写
# print(f.writable())
# 显示2行
# f.writelines(['abc\n','zx\n'])
# f.close()
# f=open('F:\Py3.5\quanzhang_study\ojbk.txt','r',encoding='utf-8')
# print(f.tell())
# f.seek(0,1)
# print(f.tell())
# f.seek(offset,whence)
#################（注意）offset代表文件的指针的偏移量，单位是字节bytes###################
#whence代表参考物，有三个取值
#0：参照文件的开头
#1：参照当前文件指针所在位置
#2: 参照文件末尾
#ps：快速移动到文件末尾f.seek(0,2
#强调：其中whence=1和whence=2只能在b模式下使用
# f=open('c.txt',mode='rt',encoding='utf-8')
#f.seek(9,0)#9鼠标右移9个位置
# print(f.tell()) # 每次统计都是从文件开头到当前指针所在位置
# with open('ojbk.txt','rb') as f:
#     print(f.tell())
#     f.seek(0,2)#鼠标移到末尾
#     print(f.tell())
##从最后一个光标seek（倒着seek用负数，2表示文件末尾)
#     f.seek(-2,2)
#     print(f.tell())
##没有seek()取最后一行（且占内存）
f=open('ojbk.txt','r')
# data=f.readlines()
# print(data[-1].decode('utf-8'))
# for i in f.readlines():#取整个文件
#     print(i)
# for i in f:
#    offs=-10
#     while true:
#         data=f.readlines()
#        if len(data)>1:
#            print('文件最后一行是%s'%(data[-1],decode('utf-8')))