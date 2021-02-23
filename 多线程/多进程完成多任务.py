import multiprocessing
import time
def sing():
    for i in range(3):
        print("唱歌。。。")
        time.sleep(0.5)
def dance():
    for i in range(3):
        print("跳舞。。。")
        time.sleep(0.5)

if __name__== '__main__':
    sing_process=multiprocessing.Process(target=sing)
    dance_process=multiprocessing.Process(target=dance)
    sing_process.start()
    dance_process.start()
