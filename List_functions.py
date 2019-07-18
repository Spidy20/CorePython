####List functions



# ###Slicing of list
# print(a[4:7])
# ##
#
# # # # #
#####Clear list :-  Clear the list elements , and it returns the empty list
a=[1,2,3,4,5,6,7]
a.clear()
print(a)

# # #####POP list :- Remove the index element which you define
b=[1,2,3,4,4,4,4,4,5,6,7]
b.pop(1)
print('after pop',b)


###Count :- it returns the count of numbers which are repeated in a list
print(b.count(4))


# # ####append :- it will add the elemnts at the last of the list
print("appending value before list",b)
b.append("kushal")
print("appending v alue before list",b)

#####Getting  value in Index
c=[1,2,3,4,'g']
print("index value of g ",c.index('g'))
#
# ####Insert index valaue
c.insert(1,'f')
print(c)

# ####reverse
c.reverse()
print(c)

# #Extend
a = [1,2,3]
b = [0,5,6]
a.extend(b)
print(a)

##SOrt
a.sort()
print(a)
#
##Copy
c = a.copy()
print(c)
print(a)


###
a = 'kushal bhavsar'
b = []
for i in a:
    b.append(i)
print(b)