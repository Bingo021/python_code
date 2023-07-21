import traceback

try:
    print("step1")
    num = 1/0
except:
    with open("d:/1.txt","a") as f:
        traceback.print_exc(file=f)