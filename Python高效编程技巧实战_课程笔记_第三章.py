# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Author: Morrow
raise Exception
# 第三章对象迭代与反迭代技巧训练_笔记
#----------3-1----------
#如何实现可迭代对象和迭代器对象-1
l = range(1,5)
iter(l) # 迭代器对象
l.__iter__() # 可迭代对象,内有__iter__方法
s = 'abc'
iter(s)
s.__getitem__() # 可迭代对象,内有__getitem__方法

#----------3-1----------

#----------3-2----------
#如何实现可迭代对象和迭代器对象-2
import requests
from collections import Iterable, Iterator

class WeatherIterator(Iterator):
	"""docstring for WeatherIterator"""
	def __init__(self, cities):
		self.cities = cities
		self.index = 0

	def getWeather(self, city):
		r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		data = r.json()['data']['forecast'][0]
		return '%s: %s , %s' % (city, data['low'], data['high'])

	def next(self):
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)

class WeatherIterable(Iterable):
	"""docstring for WeatherIterable"""
	def __init__(self, cities):
		self.cities = cities

	def __iter__(self):
		return WeatherIterator(self.cities)

for _ in WeatherIterable([u'北京', u'上海', u'广州']):
	print _

#----------3-2----------

#----------3-3----------
# 使用生成器函数实现可迭代对象
class Primenumbers(object):
	"""docstring for Primenumbers"""
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def isPrimeNum(self, k):
		if k < 2:
			return False
		for i in xrange(2, k):
			if k % i == 0:
				return False
		return True

	def __iter__(self):
		for k in xrange(self.start,self.end+1):
			if self.isPrimeNum(k):
				yield k

for _ in Primenumbers(1, 100):
	print _

#----------3-3----------

#----------3-4----------
# 如何进行反向迭代和实现反向迭代
l = xrange(1,6)
# l.reversed()
# l[::-1] 这2种方法比较浪费资源
reversed(l) # 实际等于调用l.__reversed__()
for _ in reversed(l):
	print _

class FloatRange(object):
	"""docstring for FloatRange"""
	def __init__(self, start, end, step=0.1):
		self.start = start
		self.end = end
		self.step = step
		
	def __iter__(self):
		t = self.start
		while t <= self.end:
			yield t
			t += self.step

	def __reversed__(self):
		t = self.end
		while  t >= self.start:
			yield t
			t -= self.step

f = FloatRange(1, 4, 0.5)
for i in reversed(f):
	print i

#----------3-4----------

#----------3-5----------
# 如何对迭代器做切片操作
from itertools import islice
f = open('xxx.txt')
a = islice(f, 100, 300) # 返回一个生成器对象
for i in a:
	print a
islice(f, 500) # 只切前500行
islice(f, 100, None) # 切100行到最后

#----------3-5----------

#----------3-6----------
# 如何在一个for语句中迭代多个可迭代对象
# 对象并行
from  random import randint
chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]

total = []
for c,m,e in zip(chinese, math, english):
	total.append(c+m+e)
# 对象串行
from itertools import chain
e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(41)]
e3 = [randint(60, 100) for _ in xrange(38)]
e4 = [randint(60, 100) for _ in xrange(40)]
count = 0

for s in chain(e1,e2,e3,e4):
	if s > 90:
		count += 1
#----------3-6----------

#
