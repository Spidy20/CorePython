a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

if a<b:
    if b<c:
        print("b is middle number %d" %b)
    if b>c:
        print("c is middle number %d" %c)
if a>b:

    if a<c:
        print("a is middle number %d" %a)
    if b>c:
        print("b is middle number %d" %b)
