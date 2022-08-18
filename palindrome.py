n=int(input("Enter number"))
res=0
num=n
while n>0:
    r=n%10
    res=res*10+r
    n=n//10
if num==res:
    print(res, "is palindrome")
else:
    print(res,"is not a palindrome")

