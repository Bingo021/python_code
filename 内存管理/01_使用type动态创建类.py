'''
元类：
    什么是元类？
        动态创建类
        元类->类
    用途？
        可以动态创建类
    如何使用？
    type()
        1.查看目标对象的数据类型
        2.可以使用type()，动态创建类
        语法：
        类 = type(类名,(父类...),{属性,方法})
'''
#创建一个默认父类，不包含任何属性方法的类
Person = type('Person',(),{})
#是否可以用Person创建对象
p1 = Person()
# print(p1)
# #mro()  父类是object
# print(Person.mro())

class Animal():
    def __init__(self,color):
        self.color = color
    def eat(self):
        print('动物需要吃东西')
#使用type动态创建一个类，父类就是Animal
def sleep(self):
    print('狗狗趴着睡觉')
Dog = type('Dog',(Animal,),{'age':3,'sleep':sleep})
dog = Dog('YelLow')
print(dog.age)
dog.sleep()
#是否继承了父类中的特性
#父类中的属性
print(dog.color)
#是否继承了父类的方法
dog.eat()