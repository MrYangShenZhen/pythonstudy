# import time
# class Open:
#     def __init__(self,filename,mode='r',encoding='utf-8'):
#         self.filename=filename
#         self.file=open(filename,mode,encoding=encoding)
#         self.mode=mode
#         self.encoding=encoding
#     def read(self):
#         pass
#     def write(self,line):
#         print('------------>',line)
#         t=time.strftime('%Y-%m-%d %X')#记录时间
#         self.file.write('%s %s' %(t,line))
#     def __getattr__(self, item):
#         # print(item,type(item))
#         # self.file.read
#         return getattr(self.file,item)
# f1=Open('a.txt','w+')
# # print(f1.file)
# # print(f1.__dict__)
# # print('==>',f1.read) #触发__getattr__
# # print(f1.write)
# f1.write('1111111111111111\n')
# f1.write('cpu负载过高\n')
# f1.write('内存剩余不足\n')
# f1.write('硬盘剩余不足\n')
# f1.seek(0)
# print('--->',f1.read())
# class fuck:
#     pass
# a=fuck()
# print(isinstance(a,fuck))#判断对象是否是类的实例化
# class a:
#     a=1
# class b(a):
#     pass
# class c:
#     pass
# print(issubclass(b,a))#判断B是否是A的子类
# print(issubclass(c,a))
