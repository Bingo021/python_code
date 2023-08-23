#定义一个函数
#参数 num int类型
#返回值 字符串类型
def num_fun(num:int)->str:
    return str(num)

print(num_fun(100))

#定义函数 两个参数都是int 返回int
def sum_fun(a:int,b:int)->int:
    return a+b

#定义函数参数添加默认值
def fun_test(num1:int,num2:float=12.34)->float:
    return num1+num2

# print(fun_test(10,20))
# print(fun_test(10))

#定于变量 指向一个函数
from typing import Callable
f:Callable[[int,int],int]=sum_fun
print(f(100,200))

#定义函数，产生整数生成器，每次返回一个
from typing import Iterator
def return_fun(num:int)->Iterator[int]:
    i = 0
    while i<num:
        yield i
        i+=1
print(return_fun(10))
for i in return_fun(10):
    print(i)