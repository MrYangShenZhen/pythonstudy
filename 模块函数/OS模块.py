import os
# print(os.getcwd())#打印当前文件的目录
# os.chdir('test01\test')#改变当前目录(不是改变文件位置）返回上一次..
# print(os.pardir)
# os.makedirs('test01/test')#当前目录下创建文件夹
# os.removedirs('test01/test')#删除目录中的空文件夹
# os.mkdir('test03')#生成单级目录
# os.rmdir('test')#删除单级空目录
# print(os.listdir('F:/Py3.5/quanzhang_study/'))#列出当前目录下的所有文件和子目录
# print(os.stat('元组.py'))#获取文件信息
# print(os.sep)#输出操作系统的指定分隔符
# print(os.linesep)#输出操作系统的行终止符
# print(os.pathsep)#输出分割文件路径的字符串（windows(;)
# print(os.name)#输出操作系统称呼，windows-nt,linux-posix
# print(os.path.split('F:/Py3.5/quanzhang_study/OS模块.py'))#将路径分割成目录和文件名，元组返回
#print(os.path.dirname('F:/Py3.5/quanzhang_study/OS模块.py'))#将目录返回
# print(os.path.basename('F:/Py3.5/quanzhang_study/OS模块.py'))#返回文件名
# print(os.path.exists('F:/Py3.5/quanzhang_study/OS模块.py'))#判断路径是否存在（返回布尔值）
# a='F:'#注意：路径拼接，':'后面不能接字符串会过滤掉
# b='/Py3.5/quanzhang_study/OS模块.py'
# c=os.path.join(a,b)
# print(c)
# os.makedirs('test')
# print(os.path.join(os.path.dirname(os.path.abspath(__file__)),'test','01','02'))
# os.removedirs('test')#删除，创建，只能新建，删除单级的，不能新建，删除多级。能新建，删除多级的可以新建，删除单级
# print(os.path.abspath(__file__))#斜杠与路径方向一样，取绝对路径，包含文件名
# print(os.path.dirname(__file__))#斜杠与路径方向不一样，取绝对路径，不包含文件名
# print(os.path.dirname(os.path.abspath(__file__)))#斜杠与路径方向一样，取绝对路径，不包含文件名
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#斜杠与路径方向一样。取不包含文件名的绝对路径的上一级文件夹路径
#os.path.dirname加一个就返回上一级



###########os.stat练习##############
# print(os.stat('ojbk.txt').st_size)

###