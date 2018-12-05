a={"name":"Kushal","age":18,"age":"IT Diploma"}
print(a)

#####POP
a.pop("name")
a.pop("age")

#####Fromkeys
b={"name":"Kushal","age":18,"age":"IT Diploma"}
c=('a','b','c')
b=dict.fromkeys(c,5)
print(b)

#####Copy
d={"name":"Kushal","age":18,"education":"IT Diploma"}
v=d.copy()
print(v)

####Get
print(v.get("name"))

#####Items
print(v.items())


###Update

w={"name":"","age":18,"education":"IT Diploma"}
t={"education":"IT Diploma"}
w.update(t)
print(w)


####setdefault
w.setdefault("name","kush")
print(w)
