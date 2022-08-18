class If:
    def display(self):
        a = int(input("Enter 1st number"))
        b = int(input("Enter 2nd number"))
        c = int(input("Enter 3rd number"))
        if a > b and a > c:
            print("{0} is greater than ".format(a), format(b), ",", format(c))
        elif b > a and b > c:
            print("{0} is greater than ".format(b), format(a), ",", format(c))
        else:
            print("{0} is greater than ".format(c), format(a), ",", format(b))


s = If()
s.display()