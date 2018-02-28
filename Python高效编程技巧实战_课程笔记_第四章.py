# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Author: Morrow
# raise Exception
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
#----------4-3----------
