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
print(re.match(pattern,str))
