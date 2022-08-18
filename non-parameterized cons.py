class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1
for i in range(0,5):
    s1 = Student()
print("Total count", Student.count)
