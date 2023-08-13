#导入re模块
import re
#匹配出一个字符首字母为大写字符，后边都是小写字符，这些小写字符可有可无
pattern = '[A-Z][a-z]*'
# str = 'Abc'
str = 'HEabc'
print(re.match(pattern,str))

#匹配出有效变量名
# pattern = '[A-Za-z_][a-zA-Z_0-9]*'
pattern = '[a-zA-Z_]\w*'
str = 'a'
str = 'ab'
str = '_12Abc'
str = '12abc'
print(re.match(pattern,str))

#匹配出1-99之间的数字
str = '1'
str = '10'
str = '99'
str = '9'
str = '100'
str = '199'
pattern = '[1-9]\d?'
print(re.match(pattern,str))

#匹配出一个随机密码8-20位以内（大写字母 小写字母 下划线 数字）
pattern = '\w{8,20}'
str = '123456'
str = '12345abcd'
str = '1234_qwer'
str = '12_qwerzbcd'
print(re.match(pattern,str))