"""
1.函数有了yield之后，调用它，就会生成一个生成器
2.yield的作用：程序挂起，返回相应的值。下次从下一个语句开始执行。
3.return在生成器中代表种值，直接报错：StopIeratation
4.next方法作用：唤醒并继续执行
"""


def text():
    print("start")
    i = 0
    while i < 3:
        # yield i
        temp = yield i
        print(f"temp:{temp}")
        print(f"i:{i}")
        i += 1
    print("end")
    return "done"


if __name__ == '__main__':
    a = text()
    print(a)
    a.__next__()
    a.__next__()
    a.__next__()
    a.__next__()
