def test():
    print("test function run!!!")

def test3(a,b):
    print(f"test03,{a},{b}")

def test2(func,*args,**kwargs):
    print("test2 function run...")
    func(*args,**kwargs)

a = test
test2(a)
test2(test3,100,200)