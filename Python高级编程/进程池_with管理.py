from multiprocessing import Pool
import os
from time import sleep

def func1(name):
    print(f"当前进程的ID:{os.getpid()},{name}")
    sleep(2)
    return name

if __name__ == "__main__":
   with Pool(5) as pool:
        args = pool.map(func1,('sxt1,','sxt2,','sxt3,','sxt4,','sxt5,','sxt6,','sxt7,','sxt8,'))
        for a in args:
            print(a)