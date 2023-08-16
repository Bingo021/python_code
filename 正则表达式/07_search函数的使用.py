import re

pattern = 'hello'
str = 'Hello world hello'
result = re.search(pattern,str)
print(result)
#获取匹配结果
# print(result.group())
print('match方法的使用')
r = re.match(pattern,str)
print(r)
# print(r.group())

pattern = 'love'
str = 'I love you'
print('match:',re.match(pattern,str))
print('search:',re.search(pattern,str))