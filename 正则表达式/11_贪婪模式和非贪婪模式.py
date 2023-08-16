import re
#贪婪模式
s = 'This is my tel:133-1234-1234'
pattern = r'(.+)(\d+-\d+-\d+)'
result = re.match(pattern,s)
# print(result)
# print(result.group())
# print('第一个分组匹配结果：',result.group(1))
# print('第二个分组匹配结果：',result.group(2))

#修改位非贪婪模式
s = 'This is my tel:133-1234-1234'
pattern = r'(.+?)(\d+-\d+-\d+)'
result = re.match(pattern,s)
# print(result.group())
# print('第一个分组匹配结果：',result.group(1))
# print('第二个分组匹配结果：',result.group(2))

#贪婪模式
s = 'abc123'
pattern = r'abc(\d+)'
result = re.match(pattern,s)
print(result.group(1)) #贪婪模式 匹配结果123

#非贪婪模式
pattern = r'abc(\d+?)'
result = re.match(pattern,s)
print(result.group(1))