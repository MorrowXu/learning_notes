#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Morrow
# @IDE     : PyCharm
# @File    : Python高效编程技巧实战_课程笔记_第五章.py
# @Email   : 464580843@qq.com
# Create on 2018/4/16 13:20
raise Exception
# 文件I/O高效处理案例进阶训练
#----------5-1----------
# 如何读写文本文件
# python2.x 写入文件前对unicode编码,读入文件后对二进制字符串编码
# python3.x open函数指定't'的文本模式,encoding指定编码格式
s = u'你好'
ss = s.encode('utf-8')
ss.decode('utf-8')

f = open('py2.txt', 'w')
s = u'你好'
f.write(s.encode('gbk'))
f.close()

f = open('py2.txt', 'r')
t = f.read()
print t.decode('gbk') # 你好

# f = open('py3.txt', 'wt', encoding='utf-8')   # python3  t 文本模式
# f.write('你好')
# f.close()
#
# f = open('py3.txt', 'rt', encoding='utf-8')   # python3
# s = f.read()
# print(s) # 你好

#----------5-1----------

#----------5-2----------
# 如何处理二进制文件




#----------5-2----------