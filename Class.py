class information:
    pass

i=information()
i.name=("Kushal")
i.edu=("IT")
i.enrollment=("156240316007")
i.age=("18")
print(i.name)
print(i.edu)
print(i.enrollment)
print(i.age)

print("\n")

i2=information()
i2.name=("Srushti")
i2.edu=("IT")
i2.enrollment=("156240316078")
i2.age=("20")
print(i2.name)
print(i2.edu)
print(i2.enrollment)
print(i2.age)


####USe class and object with function

print("\n")
class employe:

    def setdata(e,name,designation,age,salary):
        e.name=name
        e.designation=designation
        e.age=age
        e.salary=salary

    def getdata(e):
        print(e.name,e.designation,e.age,e.salary)

e=employe()
e.setdata("kushal","Pr manager","18","50,000")
e.getdata()

e1=employe()
e1.setdata("srushti","web developer","20","45,000")
e1.getdata()