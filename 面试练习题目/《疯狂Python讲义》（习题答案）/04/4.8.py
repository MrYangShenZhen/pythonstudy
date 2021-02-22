# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com 公众号: fkbooks                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2020, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################

# 方法一
start = 101
end = 999
for i in range(start, end + 1):
    # 计算百位上的数
    bai = i // 100
    # 计算十位、个位上的数
    shi, ge = (i - bai * 100) // 10, i % 10
    # 判断是否为水仙花数
    if ge ** len(str(i)) + shi ** len(str(i)) + bai ** len(str(i)) == i:
        print(i)
print('-' * 50)

# 方法二
end = int(input('请输入最大范围：'))
for i in range(1, end + 1):
    # 计算数字i的长度
    length = len(str(i))
    sm = 0
    temp = i
    for j in range(length):
        # 对于10求余等到个位上的数字，
        # 然后计算length次方，并累加其总和
        sm += (temp % 10) ** length
        # 将目标数缩小10倍，下一步将会获取十位上的数字
        # 依次类推，下一次获取百位、千位上的数
        temp //= 10
    # 判断是否为水仙花数
    if sm == i:
        print(i)
print('-' * 50)

# 方法三
end = int(input('请输入最大范围：'))
for i in range(1, end + 1):
    # 计算数字i的长度
    length = len(str(i))
    sm = 0
    # 将i转成字符串，然后通过遍历字符串来依次获取每位数字
    for j in str(i):
        sm += (ord(j) - 48) ** length
    # 判断是否为水仙花数
    if sm == i:
        print(i)
print('-' * 50)
    
# 方法四
end = int(input('请输入最大范围：'))
lt =[j for j in range(1, end + 1) if sum([(ord(i) - 48) ** len(str(j)) for i in str(j)]) == j]
print(lt)
print('-' * 50)
        

# 方法五（高效）
def narcissus_num(num):
    # results 存放找到的自幂数
    results = [] 
    # 定义一个长度为10的列表
    selected = [0] * 10
    # power_of_10列表依次保存[0, 10, 100, 1000, 10000, ...]
    # 该列表中的元素都是10的N次方
    power_of_10 = [10 ** i for i in range(num + 1)]
    # pre_table1 存放数字0-9的num次方的N倍（代表出现次数）的值
    # 例如num为6，pre_table1的元素依次为
    # [[0**6 * 0, 0**6 * 1, ...0**6 * 6], [1**6 * 0, 1**6 * 1, 1**6 * 2, ...]]
    pre_table1 = [[i ** num * j for j in range(num + 1)] for i in range(10)]
    # pre_table2是一个长度为10的列表，每个列表元素又是一个长度为num+1、元素为0的列表
    pre_table2 = [[0] * (num + 1) for i in range(10)]
    # num位的自幂数应该在power_of_10[num - 1]（10**num-1）～power_of_10[num]（10**num）之间
    min_num = power_of_10[num - 1]
    max_num = power_of_10[num]
    # 对pre_table2进行初始化，让它存放pre_table1中各个值除首位外的位数
    for i in range(10):
        for j in range(num + 1):
            for k in range(num, 0, -1):
                if power_of_10[k] < pre_table1[i][j]:
                    pre_table2[i][j] = k
                    break

    # 检查value是否为自幂数
    def check_narcissus(value):
        bit_result = bit_count(value)
        for i in range(10):
            if bit_result[i] != selected[i]:
                return False
        return True

    # 统计value中数字的个数，返回形如[0, 2, 2, 0, 0, 0, 0, 0, 0, 0]的列表，
    # 列表中每个元素依次代表value中0、1、2、3、4...的出现次数
    def bit_count(value):
        # 定义一个长度为10的列表
        bit_result = [0] * 10
        # 依次遍历每个位上的数，并用bit_result列表保存每个数位上的数字的出现次数。
        for i in str(value):
            bit_result[int(i)] += 1
        # 假如最后返回[0, 2, 2, 0, 0, 0, 0, 0, 0, 0]
        # 那代表该数中1出现2次、2出现2次
        return bit_result

    def pre_check(cur_index, sum, remain_num):
        cur_big = pre_table1[cur_index][remain_num]
        # 如果sum比当前数剩余最大可能数小，说明还有可能找到
        if sum < cur_big:
            return True
        max = sum + cur_big
        # 去掉cur_big的位数
        max = max // power_of_10[pre_table2[cur_index][remain_num]]
        sum = sum // power_of_10[pre_table2[cur_index][remain_num]]
        # 去掉max，sum不同的尾部。
        while not max == sum:
            max = max // 10
            sum = sum // 10
        # max，sum头部没有相同部分。
        if max == 0:
            return True
        bit_result = bit_count(max)
        # 判断大于cur_index 的所有已确定数是否在正常范围。
        for i in range(9, cur_index, -1):
            if bit_result[i] > selected[i]:
                return False
        # 判断bit_result中小于cur_index的数（从9到0还没有判断的数）的数量是否大于remain_num
        for i in range(cur_index + 1):
            remain_num -= bit_result[i]
         # 小于remain_num,属正常，返回True。
        return remain_num >= 0

    def search_num(cur_index, sum, remain_num):
        # 如果sum已经大于max_num最大值，说明已经不可能了，直接返回
        if sum > max_num:
            return
        # 如果sum加上cur_index的num次方remain_num倍，依然小于min_num最小值
        # 说明已经不可能了，直接返回
        if (sum + pre_table1[cur_index][remain_num]) < min_num:
            return

        # 如果不符合预检查，直接跳过
        if not pre_check(cur_index, sum, remain_num):
            return

        if remain_num == 0:
            # 如果检查sum符合自幂数特征，将该数添加到results列表中
            if sum > min_num and check_narcissus(sum):
                results.append(sum)
            return

        if cur_index == 0:
            selected[0] = remain_num
            # 递归调用search_num
            search_num(-1, sum, 0)
        else:
            for i in range(remain_num + 1):
                selected[cur_index] = i
                search_num(cur_index - 1, sum + pre_table1[cur_index][i], remain_num - i)
        # 对selected[cur_index]进行复位
        selected[cur_index] = 0

    # 设定初始值调用search_num，然后返回结果。
    search_num(9, 0, num)
    return results

num = int(input('请输入要计算几位的自幂数：'))
print('%d位的自幂数有:%s' % (num, narcissus_num(num)))
