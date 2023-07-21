
class MyLogDecorator():
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("日志记录")
        return self.func(*args, **kwargs)

@MyLogDecorator   #fun2 = MyLogDecorator(func)
def fun2():
    print("使用功能二")

if __name__ == '__main__':
    fun2()