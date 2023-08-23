#旧版本
oldstr = str
msg :oldstr = 'hellowold'
print('msg:',msg)
#新版本
from typing import TypeAlias
newstr :TypeAlias = str
newint :TypeAlias = int
def func_test(num:newint,msg:newstr)->newstr:
    return str(num)+msg

print(func_test(100,'类型别名更改'))