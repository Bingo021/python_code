from functools import wraps

#warps装饰器的用法
def mylog(func):
    @wraps(func)
    def infunc(*args,**kwargs):
        print("日志记录")
        print("函数文档：",func.__doc__)
        return func(*args,**kwargs)
    return infunc
@mylog
def fun2():
    """强大的功能二"""
    print("使用功能2")

if __name__ == '__main__':
    fun2()
    print("函数文档----->",fun2.__doc__)