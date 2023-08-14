import re
#匹配字符串开头 ^
pattern = '^hello.*'
str = 'hello world'
str = 'h world'
str = 'hell world'
print(re.match(pattern,str))

#匹配字符串结尾 $
#匹配一个{5，10}位的qq邮箱
pattern = '[1-9]\d{4,9}@qq.com$'
qq = '12345@qq.com'
# qq = '12345@qq.com.cn'
# qq = '12345@qq.com.cnabc'
print(re.match(pattern,qq))

#\b 匹配一个单词的边界
#左边界
str = 'abc,qwe'
str = 'abc,aqwe'
pattern = r'.*\bqwe'
print(re.match(pattern,str))

#右边界
pattern = r'.*ing\b'
str = '123 heiling'
str = '123 heilinga'
print(re.match(pattern,str))

#\B 匹配一个单词的边界
#左边界
str = 'abc,qwe'
str = 'abc,aqwe'
pattern = r'.*\Bqwe'
print(re.match(pattern,str))

#右边界
pattern = r'.*ing\B'
str = '123 heiling'
str = '123 heilinga'
print(re.match(pattern,str))