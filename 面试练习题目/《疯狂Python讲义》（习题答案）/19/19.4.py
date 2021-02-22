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
import csv, pygal

filename = 'language.csv'
x_data = ['0' + str(i + 1) for i in range(12)]
java_data = [0] * 12
python_data = [0] * 12
# 打开文件
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        # Java的数据
        if row[0] == 'java':
            java_data[int(row[2][5:]) - 1] = float(row[1])
        # Python的数据
        elif row[0] == 'python':
            python_data[int(row[2][5:]) - 1] = float(row[1])
bar = pygal.Bar()
bar.add('Java', java_data)
bar.add('Python', python_data)
bar.x_labels = x_data
bar.title = '2018年各月Java与Python市场份额对比图'
bar.x_title = '月份'
bar.y_title = '份额（%）'
bar.legend_at_bottom = True
bar.render_to_file('language.svg')
