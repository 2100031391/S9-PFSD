class Student:

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def display(self):
        print(self.id,self.name)

s1=Student(1,"ABC")
s1.display()