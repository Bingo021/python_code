#本次内容是装饰器的基础

def outfunc(func):
    def infunc(*args,**kwargs):
        print("日志记录 start...")
        func(*args,**kwargs)
        print("日志记录 end...")
    return infunc
def fun1():
    print("使用功能1")
def fun2(a,b,c):
    print("使用功能2",a,b,c)

fun1 = outfunc(fun1)
fun1()
fun2 = outfunc(fun2)
fun2(100,200,300)