def a():
    print("start in a")
    num = 10
    b(num)
    print("end in a,num is:"+str(num))

def b(s):
    s = 100
    print("run in b,s is:",str(s))

a()