import re

# 常用匹配符 . 使用匹配任意一个字符除了(\n)
pattern = '.'
str = '9'
str = 'a'
str = 'B'
str = '_'
# 定义目标式 \n
str = '\n'
# print(re.match(pattern,str))

# 常用匹配符 \d 匹配数字
str = '0'
str = '9'
str = 'a'
str = '_'
str = 'B'
# pattern = '\d'
# \D匹配非数字
pattern = '\D'
# print(re.match(pattern, str))

# 常用匹配符 \s 匹配空白字符即空格 \n \t
# pattern = '\s'
# \S匹配非空白字符串
pattern = '\S'
str = ' '
str = '\n'
str = '\t'
str = 'a'
str = '_'
str = '9'
# print(re.match(pattern,str))

#\w 匹配字母，数字，下划线
# pattern = '\w'
#\W 匹配非字母，数字，下划线
pattern = '\W'
str = '0'
str = 'a'
str = '_'
str = '\n'
# print(re.match(pattern,str))

#[]匹配列表中的字符
pattern = '[13579]'
str = '1'
str = '2'
str = '3'
str = '4'
str = 'a'
str = '_'
# print(re.match(pattern,str))

#匹配手机号码
# pattern = '\d\d\d\d\d\d\d\d\d\d\d'
pattern = '1[35789]\d\d\d\d\d\d\d\d\d'
str = '13456788756'
print(re.match(pattern,str))