a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

if a<b:
    if b<c:
        print("%d is middle number " %b)
    if b>c:
        print("c is middle number %d" %c)
else:
    if a<c:
        print("a is middle number %d" %a)
    if a>c:
        print("c is middle number %d" %c)