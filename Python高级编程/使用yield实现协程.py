import time
def func1():
    for i in range(3):
        print(f'北京：第{i}次打印啦')
        yield  # 只要方法包含了yield，就变成一个生成器
        time.sleep(1)
def func2():
    g = func1()    #func1是一个生成器，func1()就不会直接调用，需要通过next()
    print(type(g))
    for k in range(3):
        print(f'上海：第{k}次打印了' )
        next(g)   #继续执行func1的代码
        time.sleep(1)

if __name__ == '__main__':
    #有了yield，我们实现了两个任务的切换+保存状态
    start_time = time.time()
    func2()
    end_time = time.time()
    print(f"耗时{end_time-start_time}")   #耗时5.0秒，效率差别不大
