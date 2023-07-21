# 自定义异常类
class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo = errorInfo
    
    def __str__(self):
        return str(self.errorInfo)+".年龄错误！应该在1-150之间"


if __name__ == "__main__": #如果是True，则模块是作为独立文件执行，下面可以写测试代码
    age = int(input("请输入一个年龄："))
    if (age<1 or age>150):
        raise AgeError(age)
    else:
        print("正常的年龄：",age)   