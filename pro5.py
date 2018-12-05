#Example of ENCAPSULATION

class student:

    def __init__(self,passw,name,cource, sem,grade):
        if(passw=="123"):
            self.__setDetails(name,cource, sem,grade)

    def __setDetails(self,name,cource, sem,grade):
        self.name=name
        self.cource = cource
        self.sem = sem
        self.__grade=grade

    def getDetails(self):
        print(self.name, self.cource, self.sem,self.__grade)



s = student("123","Ashini","Bio","VII","A+")
s.getDetails()


