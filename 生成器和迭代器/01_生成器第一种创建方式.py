L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
#<generator object <genexpr> at 0x000001ADC444A5A0>
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
#调用__next__()方法按顺序逐个返回值