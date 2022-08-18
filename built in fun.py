class Student:
    def __init__(self, id, name, cgpa):
        self.id = id
        self.name = name
        self.cgpa = cgpa


s = Student(10, "ABC", 9.6)
print(getattr(s, "name"))  # prints name
print(getattr(s, "cgpa"))  # prints cgpa
setattr(s, "id", 3)
print(getattr(s, "id"))  # updates id to 3
print(hasattr(s, "cgpa"))  # prints True
delattr(s, "id")
# print(getattr(s,"id")) shows error because we deleted id
print(hasattr(s, "id"))  # prints false because we deleted id
