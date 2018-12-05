a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

if a<b:
    if a<c:
        print("value of a %d is Minimum"%a)
    else:
        print("value of c %d is  Minimum"%c)

else:
    if b<c:
        print("value of b %d is  Minimum"%b)
    else:
        print("value of c %d is  Minimum" % c)