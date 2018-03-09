# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Author: Morrow
raise Exception
# 第四章字符串处理技巧训练
#----------4-1----------
# 如何拆分含有多种分隔符的字符串
s = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
res = s.split(';')
t = []
map(lambda x: t.extend(x.split('|')), res)
res = t
t = []
map(lambda x: t.extend(x.split(',')), res)
res = t
t = []
map(lambda x: t.extend(x.split('\t')), res)
res = ''
for i in t:
	res += i
print res # abcdefghijklmntopqrstuvwtxyz
# 方法一
def mySplit(s, ds):
	res = [s]
	for d in ds:
		t = []
		map(lambda x: t.extend(x.split(d)), res)
		res = t
	return [x for x in res if x] # 过滤空字符串
print mySplit(s, ';|,\t')
# 方法二
import re
print re.split(r'[,;\t|]+', s)

#----------4-1----------

#----------4-2----------
# 判断字符串a是是否以b开头或结尾 str.startwith() str.endswith()
import os, stat
lst = [name for name in os.listdir() if name.endswith(('.py', '.sh'))]
a = oct(os.stat('e.py').st_mode) # 查看权限
os.chmod('e.py', os.stat('e.py').st_mode | stat.S_IXUSR)

#----------4-2----------

#----------4-3----------
#如何调整字符串中文本的格式
# 把日志文件中的日子字符串 2016-05-23 替换成 05-23-2016

import re
log = """
	2016-05-23 xxxxxxxx xxxxxxxxxxxxx
	2016-05-23 xxxxxxxx xxxxxxxxxxxxx
	2016-05-23 xxxxxxxx xxxxxxxxxxxxx
	2016-05-23 xxxxxxxx xxxxxxxxxxxxx
	2016-05-23 xxxxxxxx xxxxxxxxxxxxx
	2016-05-24 xxxxxxxx xxxxxxxxxxxxx
	2016-05-24 xxxxxxxx xxxxxxxxxxxxx
	2016-05-24 xxxxxxxx xxxxxxxxxxxxx
	2016-05-24 xxxxxxxx xxxxxxxxxxxxx
	2016-05-25 xxxxxxxx xxxxxxxxxxxxx
	"""
print re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2-\3-\1',log)
print re.sub(r'(?P<year>\d{4})-(?P<mouth>\d{2})-(?P<day>\d{2})', r'\g<mouth>-\g<day>-\g<year>',log)
# ?P<>对该捕获组取名, \g<>取出捕获组
#----------4-3----------

#----------4-4----------
# 多个字符串拼接  
lst = ['a','b','c']
''.join(lst) # 'abc'

lst = ['a', 'b',1,2,3,'c']
''.join([str(x) for x in lst]) # 如果列表很长 开销很大
''.join((str(x) for x in lst)) # 使用生成器表达式,开销低
''.join(str(x) for x in lst) # 同是生成器表达式
#----------4-4----------
