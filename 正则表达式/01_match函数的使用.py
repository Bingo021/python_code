#导入模块
import re
#定义正则表达式
pattern = 'hello'
#目标字符串
str = 'Hello world hello'
#match函数的使用
# result = re.match(pattern,str)
result = re.search(pattern,str)
#忽略大小写
# result = re.match(pattern,str,re.I)
print(result)
# print(dir(result))
print('匹配内容',result.group())
print(result.span())