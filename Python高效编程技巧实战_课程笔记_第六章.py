#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : Python高效编程技巧实战_课程笔记_第六章.py
# @Email   : 464580843@qq.com
# Create on 2018/4/16 15:02
raise Exception
# csv，json，xml,excel高效解析与构建案例进阶训练
#----------6-1----------
# 如何读写csv文件
import csv
rf = open('pingan.csv', 'rb')
rf = csv.reader(rf) # 读

wf = open('pingan_copy.csv', 'wb')
writer = csv.writer(wf)
writer.writerow(['a','b','c']) # 写

with open('pingan.csv', 'rb') as rrf: #
    reader = csv.reader(rrf)
    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)
        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)

#----------6-1----------

#----------6-2----------
# 如何读写json文件
import json
l = [1,2,'abc',{'name':'mo'}]
json.dumps(l) # 将python对象转换为json对象
json.dumps(l, separators=[',',':']) # 分隔符

json.dumps(l, sort_keys=True) # 排序

l2 = json.loads("[1,2,'abc',{'name':'mo'}]") # 将json对象转化成python对象

with open('demo.json', 'wb') as f:
    json.dump(l, f) # 接受一个文件参数

#----------6-2----------

#----------6-3----------
# 如何解析xml
from xml.etree.ElementTree import parse
f = open('demo.xml')
et = parse(f)
root = et.getroot() # 获取根节点
root.findall('country')
# 略
#----------6-3----------

#----------6-4----------
# 如何读写excel
# 使用第三方库xlrd和xlwt,分别对应读和写
import xlrd # 读
book = xlrd.open_workbook(r'C:\Users\Mo\Desktop\demo.xlsx')
# books.sheets() 得到所有sheet
sheet = book.sheet_by_index(0) # 得到第一个sheet
print sheet.nrows # 行数
print sheet.ncols # 列数
cell = sheet.cell(0, 0) # 获取单元格
print cell.value
row = sheet.row(1) # 获得一行
row2 = sheet.row_values(1) # 返回一个列表

col = sheet.col(1) # 获得列

sheet.put_cell(0,7, xlrd.XL_CELL_TEXT, u'总分', None)


import xlwt
wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
wsheet.write(0,0,'abc')
wbook.save(r'C:\Users\Mo\Desktop\demo1.xlsx')
# 略
#----------6-4----------