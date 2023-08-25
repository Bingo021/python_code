'''
垃圾回收机制：
    1.引用计数机制

    2.隔代回收机制
        原理：
            随着时间的推进，程序冗余对象逐渐增多，达到一定的数量(阈值)，系统进行回收
            (0代,1代，2代)
        代码：
            import gc
            gc.get_count()
            gc.get_threshold()      ->(700,10,10)
            gc.disable()
'''
import gc
import time


class AA():
    def __new__(cls, *args, **kwargs):
        print('new')
        return super(AA, cls).__new__(cls)

    def __init__(self):
        print('object:born at %s' % hex(id(self)))

    def __del__(self):
        print('%s 被系统回收' % hex(id(self)))


def satrt():
    while True:
        a = AA()
        b = AA()
        a.v = b
        b.v = a
        del a
        del b
        print(gc.get_threshold())
        print(gc.get_count())
        time.sleep(0.1)


# 手动关闭垃圾回收机制
# gc.disable()

gc.set_threshold(200, 10, 10)
satrt()
