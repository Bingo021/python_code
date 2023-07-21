from threading import Thread
from time import sleep


# 未使用线程同步和互斥锁的情况
class Account:
    def __init__(self, money, name):
        self.money = money
        self.name = name


# 模拟提款的操作过程
class Drawing(Thread):
    def __init__(self, drawingNum, account):
        Thread.__init__(self)
        self.drawingNum = drawingNum
        self.account = account
        self.expenseTotal = 0

    def run(self):
        if self.account.money < self.drawingNum:
            return
        sleep(1)  # 判断完可以取钱，则阻塞。就是为了测试发生冲突问题
        self.account.money -= self.drawingNum
        self.expenseTotal += self.drawingNum
        print(f"账户：{self.account.name},余额是：{self.account.money}")
        print(f"账户：{self.account.name},总共取了：{self.expenseTotal}")


if __name__ == '__main__':
    a1 = Account(100, "zjh")
    draw1 = Drawing(80, a1)  # 第一个取钱的线程
    draw2 = Drawing(80, a1)  # 第一个取钱的线程
    draw1.start()
    draw2.start()
