#旧版本
name = '张三'
age = 20
print('姓名；%s，年龄：%d'%(name,age))
#使用format
print('姓名：{}，年龄：{}'.format(name,age))
#新版本
print(f'姓名：{name}，年龄：{age}')
names = ['java','python','前端']
print(f'名称1：{names[0]}，名称2：{names[1]}')

#表达式
a = 10
b = 20
print(f'a+b运算：{a+b}')
print(f'表达式运算结果：{3*(a+b)}')