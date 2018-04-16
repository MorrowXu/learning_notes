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
# 略
#----------5-2----------

#----------5-3----------
# 如何设置文件的缓冲
f = open('demo.txt', 'w', buffering=2048) # buffering设置为大于1的整数n,n为缓冲区的大小, buffering=1为行缓冲(\n), buffering=0为无缓冲
f.write('abc')
f.close()
#----------5-3----------

#----------5-4----------
# 如何将文件映射到内存
import mmap
f = open('demo.bin','r+b')
f.fileno() # 文件描述符
m = mmap.mmap(f.fileno(), mmap.PAGESIZE*8,access=mmap.ACCESS_WRITE, offset=mmap.PAGESIZE*4)
m[0] = '\x88'

#----------5-4----------

#----------5-5----------
# 如何访问文件的状态
# 系统调用 标准库中os模块下的三个系统调用stat, fstat, lstat获取文件状态
# 标准库中os.path下一些函数, 使用起来更加简洁
import os
s = os.stat('a.txt')
stat.S_ISDIR(s.st_mode) # 判断文件类型 返回一个布尔值

# s.st_mode & stat.S_IRUSR 获取文件权限
import time
time.localtime(s.st_atime) # 获取文件最后访问时间
# s.st_size # 获取文件大小
import os
os.path.isdir('x.txt') # 判断是否是文件夹
os.path.islink('x.txt') # 判断是否是符号链接
os.path.isfile('x.txt') # 判断是否是普通文件

os.path.getatime('x.txt') # 获取最后访问时间
os.path.getsize('x.txt') # 获取文件大小
#----------5-5----------

#----------5-6----------
# 如何使用临时文件 tempfile
from tempfile import  TemporaryFile, NamedTemporaryFile
f = TemporaryFile()
f.write('abcdef' * 10000)
f.seek(0)
f.read(100)

# ntf = NamedTemporaryFile()
# ntf.name

#----------5-6----------