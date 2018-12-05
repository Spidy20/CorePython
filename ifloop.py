a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

if a>b:
    if a>c:
        print("value of a %d is maximum"%a)
    else:
        print("value of c %d is maximum"%c)

else:
    if b>c:
        print("value of b %d is maximum"%b)
    else:
        print("value of c %d is maximum" % c)
