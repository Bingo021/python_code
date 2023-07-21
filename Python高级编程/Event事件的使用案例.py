import threading
import time


def chihuoguo(name):
    #等待事件，进入阻塞状态
    print(f"{name}已经启动")
    print(f"小伙伴{name}已经进入就餐状态！")
    time.sleep(1)
    event.wait()
    #收到事件后进入运行状态
    print(f"{name}收到通知了")
    print(f"小伙伴{name}开始吃喽")

if __name__ == '__main__':
    event = threading.Event()
    #创建新线程
    thread1 = threading.Thread(target=chihuoguo,args=("tom",))
    thread2 = threading.Thread(target=chihuoguo,args=("cherry",))
    #开启线程
    thread1.start()
    thread2.start()
    time.sleep(10)
    #发送事件通知
    print("------->>>主线程通知小伙伴开吃喽！")
    event.set()