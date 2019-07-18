# a=int(input("enter the value of a:"))
# factorial = 1
#
# if (a < 0):
#    print("Sorry, factorial does not exist for negative numbers")
# elif (a== 0):
#    print("The factorial of 0 is 0")
# else:
#    for i in range(1,a + 1):
#        factorial = factorial*i
#    print("The factorial of", a,"is",factorial)
a = int(input("enter value:" ))
factorial = 1


try:

    if (a <0):
        print ("sorry")
    elif (a == 0):
        print ("can't do it")
    else:
        for i in range (1, a+1):
            factorial = factorial*i
    print("end state:", factorial)

except Exception as e:
    print(e)