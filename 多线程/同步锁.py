
import threading,time
lock=threading.Lock()
def sum():
    global num
    # num-=1
    lock.acquire()#加上锁，使以下代码线程串联执行
    NUM=num
    time.sleep(0.001)
    '''加上等待时间，CPU会在未处理完该线程情况下切换去处理其它线程，
    当遍历执行其它线程，达到0.001S导致第一个线程有机会执行下一步-1操作。会使部分能正常-1.
    大部分只赋予了值未-1，遍历最后那个线程结束操作'''
    num=NUM-1
    lock.release()#释放锁，使后面代码正常

num=100
l=[]
for i in range(100):
    t=threading.Thread(target=sum)
    t.start()
    l.append(t)
for t in l:
    t.join()

print(num)