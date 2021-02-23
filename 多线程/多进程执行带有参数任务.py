import multiprocessing
import time
import os
def sing(num,name):
    for i in range(num):
        print("唱歌主进程的pid:", os.getpid())
        print("唱歌父进程的pid:", os.getppid())
        print("%s唱歌。。。"%name)
        time.sleep(0.5)
def dance(num,name):
    for i in range(num):
        print("跳舞主进程的pid:", os.getpid())
        print("跳舞父进程的pid:", os.getppid())
        print("%s跳舞。。。"%name)
        time.sleep(0.5)

if __name__== '__main__':
    # 获取当前运行文件的主进程编号
    print("主进程的pid:", os.getpid())
    #args元组方式传参.需要按照函数入参顺序传递
    sing_process=multiprocessing.Process(target=sing,args=(3,'小明'))
    #字典方式传参kwargs，仅保证字典的key跟函数入参相同
    dance_process=multiprocessing.Process(target=dance,kwargs={"num":2,"name":"小丽"})
    sing_process.start()
    dance_process.start()
