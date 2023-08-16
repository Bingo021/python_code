import re
pattern = 'aa|bb|cc'
# str = 'aa'
# print(re.match(pattern,str))
# print(re.search(pattern,'where is bb'))

#匹配0-100之间的数字
s = '0'
s = '9'
s = '10'
s = '99'
s = '100'
s = '101'
s = '1000'
pattern = r'[1-9]?\d$|100$'
print(re.match(pattern,s))

#'[xyz]'和'x|y|z'
pattern = '[xyz]'
pattern1 = 'x|y|z'
print(re.match(pattern,'y'))
print(re.match(pattern1,'y'))
#区别
#匹配第一个字母是a或b 第二个字母可以是c或者d 结果ac，ad，bc，bd
print(re.match('[ab][cd]','acge'))

print(re.match('ab[cd]','abc'))

print(re.match('ab|cd','ac'))