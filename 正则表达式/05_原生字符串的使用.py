import re
s = 'c:\\a\\c'
print(s)
#反斜杠作为转意义
s = '\n123'
print(s)
s = '\\n123'
print(s)
#使用原生字符串 r
s = r'\n123'
print(s)

#在正则表达式中反斜杠作为转义
s = '\n123'
pattern = '\\n\d{3}'
print(re.match(pattern,s))

#目标字符串
s = '\\n123'
s = '\\\\n123'
pattern = '\\n\d{3}'
print('\\n\d{3}:',re.match(pattern,s))

#使用原生字符串
s = '\\n123'
pattern = r'\\n\d{3}'
print(re.match(pattern,s))