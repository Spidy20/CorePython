class student:

     def setDetails(self,name,cource,sem):
        self.name=name
        self.cource=cource
        self.sem=sem

     def getDetails(self):
         print(self.name,self.cource,self.sem)

     def marks(marks,python,java):
         marks.python=python
         marks.java=java
         print(int(marks.java)+int(marks.python))



s=student()
s.setDetails("Ashini","Bio","VII")
s.getDetails()
s.marks(90,80)

s1=student()
s1.setDetails("Kushal","Diploma","VII")
s1.getDetails()
s1.marks(90,90)
