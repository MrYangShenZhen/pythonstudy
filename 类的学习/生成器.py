def test(val,step):#类似与迭代器
    print("函数开始执行>>>>>>>")
    cur=0
    for i in range(val):
        cur += i*step
        # print(cur,end='')
        yield cur #执行时关闭程序
t=test(10,2)
print('>>>>>>>>>>>')
print(next(t))
print(next(t))