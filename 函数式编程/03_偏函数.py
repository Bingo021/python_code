import functools


def int2(x,base=2):
    return int(x,base)

print(int2('1000000')) #64
print(int2('1010101')) #85

#调用工具库定义偏函数
int3 = functools.partial(int,base=2)
print(int3("1010101"))
print(int3("1010101",base=10))