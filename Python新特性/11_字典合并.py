dick1 = {'a':1}
dick2 = {'b':2}
#旧版本
# dick1.update(dick2)
# print(dick1)

#新版本
result = dick1 | dick2
print(result)