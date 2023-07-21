#在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2==1

L=filter(is_odd,[1,2,4,5])
print(list(L))

L = filter(lambda n:n%2==1,[1,2,4,5])
print(list(L))