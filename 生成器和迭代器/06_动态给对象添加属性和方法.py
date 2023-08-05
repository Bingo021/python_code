import types


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("zhangjiahao", 23)
p2 = Person("zhoumong", 20)

# 动态的给对象添加属性和方法
p1.score = 100
print(p1.score)


def run(self):
    print(f"{self.name} is {self.age} years old,running")


# 动态的给对象添加方法
p1.run = types.MethodType(run, p1)
p1.run()
