import re
#  * 匹配0次或多次
pattern = '\d*'
str = 'abc'
print(re.match(pattern,str))

# + 匹配1次或者多次
pattern = '\d+'
str = '12abc'
print(re.match(pattern,str))

# ? 匹配1次或者0次
pattern = '\d?'
str = '1234abc'
print(re.match(pattern,str))

# {m} 重复m次
pattern = '\d{4}'
str = '1234abc'
print(re.match(pattern,str))

# {m,n} 重复至少是m次
pattern = '\d{4,}'
str = '12345abc'
print(re.match(pattern,str))

# {m,n} 重复匹配m到n次
pattern = '\d{4,6}'
str = '1234567abc'
print(re.match(pattern,str))