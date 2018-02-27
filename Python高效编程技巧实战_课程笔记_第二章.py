# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Author: Morrow
raise Exception
# 第二章数据结构与算法进阶训练_笔记
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

#----------2-3----------
# 统计序列中元素的频度
data = [randint(0,20) for _ in xrange(20)]
c = dict.fromkeys(data, 0)
for x in data:
	c[x] += 1

from collections import Counter
c2 = Counter(data)
c2.most_common(3)

# 单词频率统计
# import re
# f = open('xxx.txt').read()
# lst = re.split('\w+', f)
# c3 = Counter(lst)
# c3.most_common(10) # 得出频率最高的前10单词

#----------2-3----------

#----------2-4----------
# 对字典中的项排序
d = {x: randint(60,100) for x in 'xyzabc'}
result = sorted(zip(d.itervalues(), d.iterkeys())) # 方法一,zip后sorted
sorted(d.items(), key=lambda x: x[1]) # 方法二, 改sorted默认排序参数

#----------2-4----------

#----------2-5----------
# 快速找到多个字典中的公共键
from random import randint, sample
s1 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))} # sample('abcdefg', randint(3,6)) 随机取样
s2 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}
s3 = {x: randint(1,4) for x in sample('abcdefg', randint(3,6))}

# 方法一
res = []
for k in s1:
	if k in s2 and k in s3:
		res.append(k)

# 方法二
res = s1.viewkeys() & s2.viewkeys() &s3.viewkeys() # 集合交集操作

# 方法三
reduce(lambda a,b: a&b, map(dict.viewkeys(), [s1,s2,s3]))  # map得到每轮的集合,再用reduce进行与运算操作

#----------2-5----------

#----------2-6----------
# 如何让字典保持有序
from collections import OrderedDict
from time import time
d = OrderedDict()
players = list('ABCDEFGH')
start = time()

for i in xrange(8):
	raw_input()
	p = players.pop(randint(0, 7-i))
	end = time()
	print i + 1, p, end - start
	d[p] = (i + 1, end - start)

#----------2-6----------

#----------2-7----------
# 实现用户的历史记录功能
from collections import deque # 双端队列

N = randint(0, 100)
history = deque([], 5)

def guess(K):
	if K == N:
		print 'right'
		return True
	if K < N:
		print '%s is less-than N' % K
	else:
		print '%s is greater-than N' % K
	return False

while True:
	line = raw_input('please input a number: ')
	if line.isdigit():
		K = int(line)
		history.append(K)
		if guess(K):
			break
	elif line == 'history' or line == 'h?':
		print list(history)
# 对象存储
import pickle
pickle.dump(q, open('history', 'w'))
q2 = pickle.load(open('history'))


#----------2-7----------
