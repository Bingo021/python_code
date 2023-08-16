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