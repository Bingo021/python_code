'''
类装饰器：
    在不修改函数源代码的前提下，新增的功能
'''

class AAA():
    def __init__(self,func):
        # print('我是AAA.init')
        # print(func.__name__)
        self._func = func

    # TypeError: 'AAA' object is not callable
    def __call__(self, *args, **kwargs):
        # print('在这可以实现任何功能')
        self.addFunc()
        self._func()

    def addFunc(self):
        print('用户权限验证')
        print('日志系统处理')

@AAA
# test1 = AAA(test1)
def test1():
    print('我是功能1')

test1()