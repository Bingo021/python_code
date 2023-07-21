while True:
    try:
        x = int(input("请输入一个数字："))
        print("您输入的数字是：",x)
        if x == 88:
            print("退出程序")
            break
    except:
        print("异常！输入的不是数字！")