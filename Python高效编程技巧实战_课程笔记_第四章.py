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

#----------4-5----------
# 如何对字符串进行左, 右, 居中对齐
# 方法一
# 使用字符串的 str.ljust() str.rjust() str.center()
s = 'abc'
s.ljust(20) # 20代表宽度
# 'abc                 '
s.ljust(20, '=') # 宽度20, 用=号填充
# 'abc================='
s.rjust(20)
# '                 abc'
s.center(20)
# '        abc         '

# 方法二
# 使用format()方法,传递类似'<20>', '>20', '^20'参数完成
s = 'abc'
format(s, '<20')
# 'abc                 '
format(s, '>20')
# '                 abc'
format(s, '^20')
# '        abc         '
# 取字典中键的最大宽度
max(map(len, d.keys()))
#----------4-5----------

#----------4-6----------
# 去掉字符串中不需要的字符
# 方法一 字符串strip(),lstrip(),rstrip()方法去掉字符串两端字符
s = '   abc 123   '
s.strip()
# 'abc 123' lstrip 去掉左边 rstrip 去掉右边
s = '---abc+++'
s.strip('-+') # '-+' 代表需要去掉的符号
# 'abc' 

# 方法二 删除单个固定位置的字符,可以使用切片+拼接的方法
s = 'abc:123'
s[:3] + s[-3:] # s[:3] + s[4:]

# 方法三 字符串的replace()方法或者正则表达式的re.sub()删除任意位置字符
s = '\tabc\t123\txyz'
s.replace('\t', '')
# 'abc123xyz'
import re
s = '\tabc\t123\txyz\ropq\r'
re.sub(r'[\t\r]', '', s)
# 'abc123xyzopq'

# 方法四 字符串translate()方法, 可以同时删除多种不同的字符.
s = 'abc12314324432xyz' # 对该字符串加密 a=x b=y c=z x=a y=b z=c 建立这种映射表
import string
cc = string.maketrans('abcxyz','xyzabc') # 利用string 函数建立映射表,string.maketrans方法返回一个映射表
s.translate(cc)
# 'xyz12314324432abc'
s = 'abc\refg\n234324\t' # 删除\r\n\t
s.translate(None, '\r\n\t')
# 'abcefg234324'
# unicode 音标转换 略

#----------4-6----------
