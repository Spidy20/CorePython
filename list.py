mylist= ["Bhavsar Kushal","Diploma in IT","SPI in last sem= 8.82",156240316007,"favourate subject: python,android,.NET","address=Saraspur","College=GP himatnagar"]
print(mylist[-1])
print(mylist[:3])####slicing
print(mylist[0:3])


### Repeatation
print(mylist*5)

##membership (IN, NOT IN)
a=[4,5,6]
b=[1,2,3]
if (5 in b):
    print("2 in b list")
else:
    print("not found")

###concate
c=a+b
print("new list  c",c)

###Itration
for k in c:
    print(k)

###Update list
d=[1,2,3,4,5]
d[2]=6
print("list d\n",d)


####Delete List

del d
print(d)
