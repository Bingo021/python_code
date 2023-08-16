import re
#匹配座机号码 区号{3,4}-电话号码{5,8}
pattern = r'\d{3,4}-[1-9]\d{4,7}$'
s = '010-1234567'
# s = '010-123456789'
result = re.match(pattern,s)
print(result)

#使用分组
pattern = r'(\d{3,4})-([1-9]\d{4,7}$)'
s = '010-1234567'
# s = '010-123456789'
result = re.match(pattern,s)
# print(result)
# print(result.group())
# print('第一个分组：',result.group(1))
# print('第二个分组：',result.group(2))
# print('groups():',result.groups())
# print('第一个分组：',result.groups()[0])
# print('第二个分组：',result.groups()[1])

#\num的使用
s = '<html><head>分组的使用</head></html>'
# s = '<html><head>分组的使用</body></h1>'
pattern = r'<.+><.+>.+</.+></.+>'

#优化正则表达式
pattern = r'<(.+)><(.+)>.+</\2></\1>'
print(re.match(pattern,s))

#(?P<别名>)
#引用 (?P=别名)
s = '<html><head>分组的使用</head></html>'
pattern = r'<(?P<k1>.+)><(?P<k2>.+)>.+</(?P=k2)></(?P=k1)>'
print(re.match(pattern,s))
