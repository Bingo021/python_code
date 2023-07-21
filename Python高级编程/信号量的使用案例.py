#一个房间，一次只允许两个人进入
from threading import Semaphore, Thread
from time import sleep

def home(name,se):
    se.acquire()
    print(f"{name}进入房间")
    sleep(3)
    print(f"*****{name}走出房间")
    se.release()

if __name__ == '__main__':
    se = Semaphore(2)  #创建信号量对象
    for i in range(7):
        t = Thread(target=home,args=(f"tom{i}",se))
        t.start()
