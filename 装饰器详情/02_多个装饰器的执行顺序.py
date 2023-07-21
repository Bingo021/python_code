import time

def mylog(func):
    print("mylog,start!")

    def infunc(*args,**kwargs):
        print("日志记录,satrt!")
        func(*args,**kwargs)
        print("日志记录,end!")

    print("mylog,end!")
    return infunc

def cost_time(func):
    print("cost_time,start!")

    def infunc(*args, **kwargs):
        print("开始计时,satrt!")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"耗费时间：{end-start}")

    print("cost_time,end!")
    return infunc
@mylog
@cost_time
def fun(a,b):
    print(f"fun:{a},{b},start!")
    time.sleep(3)
    print("fun,end!")

fun(200,300)