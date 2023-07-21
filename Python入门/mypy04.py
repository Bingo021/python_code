try:
    a = input("请输入被除数：")
    b = input("请输入除数：")
    c = float(a)/float(b)

except ZeroDivisionError:
    print("异常：除数不能为0")
except TabError:
    print("异常：除数和被除数都应该为数值类型")
except BaseException as e:
    print(e)
    print(type(e))
else:
    print(c)
finally:
    print ("我是finally语句，无论是否发生异常，我都会被执行！！！")

print("程序结束！")