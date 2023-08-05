class MyNombers:
    def __iter__(self):
        self.num = 10
        return self

    def __next__(self):
        if self.num<40:
            x=self.num
            self.num +=10
            return x
        else:
            raise StopIteration

myclass = MyNombers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
