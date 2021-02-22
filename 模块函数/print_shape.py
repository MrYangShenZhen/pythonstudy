my_list=['Python','Kotlin','Swift']
def print_triangle(n):
    #打印由星号组成的三角形
    if n <= 0:
        raise ValueError('n必须大于0')
    for i in range(n):
        print(''*(n-i-1),end='')
        print('*'*(2*i+1),end='')
        print('')

#=========以下是测试代码===========
def test_print_triangle():
    print_triangle(3)
    print_triangle(4)
    print_triangle(7)
if __name__=='__main__':
    test_print_triangle()