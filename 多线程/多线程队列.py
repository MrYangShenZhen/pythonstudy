import queue
# # q=queue.Queue(3)#Queue()可传数字，表示该队列可存五组数据
# q=queue.LifoQueue(3)#后进先出模式
'''创建线程队列，默认先进先出'''
# q.put('你好')
# q.put(2)
# q.put({"lesson":"math"})
# q.put('test',False)#会提示满了的报错
# while 1:
#     data=q.get()
#     print(data)
#put,get在队列满了或者为空时去put,get会导致程序一直在运行中

'''优先级模式'''
# Q=queue.PriorityQueue(3)
# Q.put([2,'你好'])
# Q.put([1,2])
# print(Q.full())
# Q.put([3,{"lesson":"math"}])
# print(Q.full())
# while 1:
#     Data=Q.get()
#     print(Data[1])
#     print(Q.empty())