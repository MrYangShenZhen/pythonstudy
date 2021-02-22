import threading
import time

def game():
    print("game start %s"%time.ctime())
    time.sleep(3)
    print("game stop %s"%time.ctime())


def music():
    print("music start %s"%time.ctime())
    time.sleep(6)
    print("music stop %s"%time.ctime())





if __name__=="__main__":
    t1=threading.Thread(target=game)
    t2=threading.Thread(target=music)
    # t1.setDaemon(True)#与join方法相反，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出
    t1.start()#开始运行t1对象关联的函数game
    # t2.setDaemon(True)
    t2.start()
    #t2.run()#报错，不清楚
    a=t1.isAlive()
    print(a)
    # t1.join()#后面程序的运行要等t1子线程运行完，才能接着运行
    print("ending")