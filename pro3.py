class student:

     def setDetails(self,name,cource,sem):
        self.name=name
        self.cource=cource
        self.sem=sem

     def getDetails(self):
         print(self.name,self.cource,self.sem)

     def marks2(marks3,python,java):
         marks3.python=python
         marks3.java=java
         print(int(marks3.java)+int(marks3.python))


s,s1,s2=student()

name1=input('Enter name:')
sub1=input('Enter Subject:')
c1=input('Enter class:')
s.setDetails(name1,sub1,c1)
s.getDetails()
s.marks2(90,80)


s1.setDetails("Kushal","Diploma","VII")
s1.getDetails()
s1.marks2(90,90)


s2.setDetails('Atharva','MTECH','VII')
s2.getDetails()
s2.marks2(80,80)