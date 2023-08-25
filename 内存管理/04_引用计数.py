'''
垃圾回收机制:
    Python:
    1.引用计数机制为主
        如何获取一个对象的引用计数？
            sys.getrefcount(a)
            刚创建对象引用计数为2
        a.增加引用计数操作
            1.如果有新的对象使用该对象，+1
            2.装进列表+1
            3.作为函数参数
        b.减少引用计数操作
            1.如果有新的对象使用该对象，新对象不再使用
            2.从列表中移除-1
            3.函数调用结束
            4.del显示销毁
    2.隔代回收为辅助
    循环引用
'''
import sys
class AA():
    #创建对象开辟内存时调用
    def __new__(cls, *args, **kwargs):
        print('开辟内存空间')
        return super(AA,cls).__new__(cls)
    #初始化方法
    def __init__(self):
        print('创建对象at:%s'%hex(id(self)))
    #对象被系统回收之前，会调用该方法
    def __del__(self):
        print('%s say bye bye'%hex(id(self)))

def test1(aaa):
    print(aaa)
    print('a的引用计数为：%d' % sys.getrefcount(a))

a = AA()
print('a的引用计数为：%d'%sys.getrefcount(a))
b = a
print('a的引用计数为：%d'%sys.getrefcount(a))
list1 = [a]
print('a的引用计数为：%d'%sys.getrefcount(a))
test1(a)
print('a的引用计数为：%d'%sys.getrefcount(a))
print('*'*40)

b = 100
print('a的引用计数为：%d'%sys.getrefcount(a))
list1.remove(a)
print('a的引用计数为：%d'%sys.getrefcount(a))

print('--------------程序结束------------------')
