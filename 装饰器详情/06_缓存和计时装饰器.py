import time

class CacheDecorator():
    __cache={}
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        #如果缓存中有对应的方法名，则直接返回对应的返回值
        if self.func.__name__ in CacheDecorator.__cache:
            return CacheDecorator.__cache[self.func.__name__]
        #如果缓存中没有对应的方法名，则进行计算，并将结果缓存
        else:
            result = self.func(*args, **kwargs)
            CacheDecorator.__cache[self.func.__name__] = result
            return result

def cost_time(func):
    def infunc(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"耗时：{end-start}")
        return result
    return infunc
@cost_time
@CacheDecorator
def fun1_long_time():
    """模拟耗时较长，每次执行返回结果都一样的情况"""
    print("start fun1")
    time.sleep(3)
    print("end fun1")
    return 999

if __name__ == '__main__':
    r1 = fun1_long_time()
    r2 = fun1_long_time()
    print(r1)
    print(r2)