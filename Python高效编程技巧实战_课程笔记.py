# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Author: Morrow

#----------2-1----------
# 过滤
from random import randint

data = [1,5,-3,-2,6,0,9]
res = []
for x in data:
	if x >= 0:
		res.append(x)
print res

# filter函数
res1 = filter(lambda x:x >= 0, data)
print res1

# 列表解析 
res2 = [x for x in data if x >= 0]
print res2

# 字典解析
d = {x:randint(60,100) for x in xrange(1,21)}
res3 = {k:v for k,v in d.iteritems() if  v > 90}
print res3

# 集合解析
s = set(data)
res4 = {x for x in s if x % 3 == 0}
print res4
# ipython里测试性能可以用timeit

#----------2-1----------

#----------2-2----------
# 元组命名,提高程序可读性
# 方法一, 定义常量

NAME,AGE,SEX,EMAIL = xrange(4)
student = ('Jim',16,'male','jim8721@gmail.com')
#name
print student[NAME]
#age
if student[AGE] >= 18:
	pass
#sex
if student[SEX] == 'male':
	pass

# 方法二, nametuple
from collections import namedtuple

Student = namedtuple('Student', ['name','age','sex','email'])
s = Student('Jim',16,'male','jim8721@gmail.com')
print s # Student(name='Jim', age=16, sex='male', email='jim8721@gmail.com')
print s[0],s.name,isinstance(s, tuple) # Jim

#----------2-2----------