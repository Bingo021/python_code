#需求：实现变量a自增
#通过自由变量，可以实现递增，也不会污染其他程序
a = 10
def add():
    a = 10
    def increment():
        nonlocal a
        a += 1
        print("a:",a)
    return increment

def print_ten():
    if a == 10:
        print("ten!!!")
    else:
        print("全局变量a，不等于10")

increment = add()
increment()
increment()
increment()
print_ten()