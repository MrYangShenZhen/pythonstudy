import multiprocessing
import time
def work():
    for i in range(10):
        print("唱歌。。。")
        time.sleep(0.2)
    # print('子进程运行结束')

if __name__== '__main__':
    work_process=multiprocessing.Process(target=work)
    #默认主进程运行结束，主进程也会等子进程运行后再结束
    #设置守护主进程。即主进程运行结束子进程也运行结束
    work_process.daemon=True
    work_process.start()
    time.sleep(1)
    print("主进程运行结束")