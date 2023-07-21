from multiprocessing import Process, Queue
from time import sleep

class MyProcess(Process):
    def __init__(self,name,mq):
        Process.__init__(self)
        self.name = name
        self.mq = mq

    def run(self):
        print(f"Process:{self.name},start")
        print(f"get Data:{self.mq.get()}")
        sleep(2)
        self.mq.put(f"New Data:{self.name}")
        print(f"Process:{self.name},end")

if __name__ == '__main__':
    mq = Queue()
    mq.put("1")
    mq.put("2")
    mq.put("3")

    #进程列表
    p_list = []
    for i in range(3):
        p = MyProcess(f"p{i}",mq)
        p_list.append(p)
    for p in p_list:
        p.start()

    for p in p_list:
        p.join()

    print(mq.get())
    print(mq.get())
    print(mq.get())
