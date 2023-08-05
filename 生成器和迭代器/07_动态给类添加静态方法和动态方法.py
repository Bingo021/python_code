class Person():
    pass


@staticmethod
def staticfunc():
    print("---static method---")


Person.staticfunc = staticfunc
Person.staticfunc()
Person.score = 1000


@classmethod
def clsfunc(cls):
    print("---cls method---")


Person.clsfunc = clsfunc
Person.clsfunc()
