a=int(input("enter the value of a:"))

try:
    c=a/0

except Exception as e:
    print(e)