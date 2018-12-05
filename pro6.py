#Example of INHARITENCE

#Parent class
class student:

    def setDetails(self,name,cource, sem,grade):
        self.name=name
        self.cource = cource
        self.sem = sem
        self.__grade=grade

    def getDetails(self):
        print(self.name, self.cource, self.sem,self.__grade)

#Child class
class student_marks(student):
    def marks(self,python,java):
        self.python=python
        self.java=java
        print(int(self.python)+int(self.java))

s = student_marks()
s.setDetails("Ashini","Bio","VII","A+")#Parent class method
s.marks(90,80)#Child class method
s.getDetails()#Parent class method
