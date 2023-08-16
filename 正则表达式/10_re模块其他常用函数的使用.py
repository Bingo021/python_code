import re
#sub和subn
phone = "2004-959-559 # 这是一个外国电话号码"

#替换目标字符串中注释
pattern = r'#.*'
result = re.sub(pattern,'',phone)
# print(result)

#删除非数字的字符串 \D
pattern = r'\D'
result = re.sub(pattern,'',phone)
# print(result)

#调用subn
result = re.subn(pattern,'',phone)
# print(result)
# print('替换的结果：',result[0])
# print('替换的次数：',result[1])

#compile
s = 'one1 two2 3 4_'
pattern = r'\w+'
regex = re.compile(pattern)
# print(regex.match(s))
# print(re.match(pattern,s))

#findall()
pattern = r'\w+'
s = 'ab c d 1 2 _ helloworld # ac @'
result = re.findall(pattern,s)
# print(result)
# print(re.match(pattern,s))
# print(re.search(pattern,s))

#finditer()
result = re.finditer(pattern,s)
# print(result)
# for i in result:
#     print(i.group())

#splist()
s = 'a 1 b 2 c 3 d'
pattern = r'\d+'
result = re.split(pattern,s)
print(result)

#指定分隔的次数
print(re.split(pattern,s,maxsplit=2))