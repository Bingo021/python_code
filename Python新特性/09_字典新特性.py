data = {'a':1,'b':2,'c':3}
print('字典数据：',data)
#items values keys
print('items:',data.items())
print('values:',data.values())
print('keys:',data.keys())

#新特性
keys = data.keys()
items = data.items()
values = data.values()
print('mapping:',keys.mapping)
print('mapping:',items.mapping)
print('mapping:',values.mapping)

#旧版本
keys = ['name','age','sex']
values = ['zs',23,'man']
data_dict = dict(zip(keys,values))
print('创建字典对象：',data_dict)

#新版本
data_dict2 = dict(zip(keys,values,strict=True))
print('新版添加strict属性：',data_dict2)
