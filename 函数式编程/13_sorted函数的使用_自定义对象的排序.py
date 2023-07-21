class Student:
    def __init__(self,age,name):
        self.name = name
        self.age = age

if __name__ == '__main__':
    stu1 = Student(41,'aaa')
    stu2 = Student(21,'bbb')
    stu3 = Student(31,'ccc')
    student_list = sorted([stu1,stu2,stu3],key=lambda x:x.age)
    for stu in student_list:
        print(f"{stu.name}----{stu.age}")