class Methodoverloading:
    def display(self,num=10):
        return num;
obj=Methodoverloading()
print(obj.display())
print(obj.display(30))
