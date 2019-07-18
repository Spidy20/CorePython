#Example of ENCAPSULATION
class student:
    def __init__(self,passw,name,cource, sem,grade):
        if passw == '123':
            self.__setDetails(name,cource, sem,grade)
        else:
            print('Andhe password galat he')

    def __setDetails(self,name,cource, sem,grade):
        self.name=name
        self.cource = cource
        self.__sem = sem
        self.grade=grade

    def getDetails(self):
        print(self.name, self.cource, self.__sem,self.grade)

s = student('12345', "Ashini", "Bio", "VII", "A+")
s.getDetails()