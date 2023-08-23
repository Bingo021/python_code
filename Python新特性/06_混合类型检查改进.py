#j旧版本的使用
from typing import Union
def old_func_test(num:Union[int,float])->Union[int,float]:
    return num+100

print(old_func_test(10))
print(old_func_test(10.23))

#新版本中 |
def new_func_test(num:int|float)->int|float:
    return num+100
print(new_func_test(10))
print(new_func_test(10.23))