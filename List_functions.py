####List functions
a=[1,2,3,4,5,6,7,8]

####Finding length of list
print(len(a))


####Find max & min value
print(min(a))
print(max(a))

####Tuple
tup=(1,2,3,4,5,6)
print(tup)
print(type(tup))

####Tuple to list
l=list(tup)
print(l)
print(type(l))



#####Clear list
a=[1,2,3,4,5,6,7]
a.clear()
print(a)

#####POP list
b=[1,2,3,4,4,5,6,7]
b.pop(1)

####Count
print(b.count(4))

####append
print("appending value before list",b)
b.append("kushal")
print("appending v alue before list",b)


#####Getting  value in Index
c=[1,2,3,4,'g']
print("index value of c ",c.index(5))


####Insert index valaue
c.insert(1,'f')
print(c)

####reverse
c.reverse()
print(c)





