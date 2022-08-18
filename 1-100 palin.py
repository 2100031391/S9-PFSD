n=1
for x in range(1,100):
    res = 0
    num = n
    while n > 0:
        r=n%10
        res=res*10+r
        n=n//10
    if num==res:
        print(x,end=" ")

