try:
    f = open("d:/1.txt","r")   #read r
    content = f.readline()
    print(content)
except BaseException as e:
    print(e)
finally:
    print("关闭文件")
    f.close()

print("继续执行其他代码")
print("程序结束")