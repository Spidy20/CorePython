a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

if a>b>c:
    print("A IS MAX")
    print("B IS MID")
    print("C IS MIN")

if a<b<c:
    print("C IS MAX")
    print("B IS MID")
    print("A IS MIN")

if a<b>c:
    if a>c:
        print("B IS MAX")
        print("A IS MID")
        print("C IS MIN")
    if c>a:
        print("B IS MAX")
        print("C IS MID")
        print("A IS MIN")


if a>b<c:
    if a>c:
        print("A IS MAX")
        print("C IS MID")
        print("B IS MIN")
    if c>a:
        print("C IS MAX")
        print("A IS MID")
        print("B IS MIN")