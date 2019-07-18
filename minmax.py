a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))

##max

if a>b:
    if a>c:
        print("a is a maximum number %d" %a)
    if a<c:
        print("c is a maximum number %d" %c)
else :
    if b>c:
        print("b is a maximum number %d" %b)
    if b<c:
        print("c is a maximum number %d" %c)


###Min
if a<b:
    if a<c:
        print("a is minimum number " ,a)
    if a>c:
        print("c is minimum number ",c)
else:
    if b<c:
        print("b is minimum number ",b)
    if b>c:
        print("c is minimum number ",c)

#####Middle number

if a<b:
    if b<c:
        print("b is middle number %d" %b)
    if b>c:
        print("c is middle number %d" %c)
if a>b:

    if a<c:
        print("a is middle number %d" %a)
    if a>c:
        print("c is middle number %d" %b)

####equal

if a==b<c:
     print("a and b value is equal and minimum and c value is maximum")

if a==b>c:
    print("a and b value is equal and maximum and c value is minimum")

if b==c<a:
    print("b and c value is equal and minimum and a value is maximum")
if b==c>a:
    print("b and c value is equal and maximum and a value is minimum")

if c==a<b:
    print("c and a value is equal and minimum and b value is maximum")
if c==a>b:
    print("c and a value is equal and maximum and b value is minimum")