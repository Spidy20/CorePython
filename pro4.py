#Example of constructor (Initilization)

class student:

    def __init__(self,name):
        self.name=name

    def setDetails(self,cource, sem):
        self.cource = cource
        self.sem = sem

    def getDetails(self):
        print(self.name, self.cource, self.sem)

try:
    s = student('Srushti')
    s.setDetails("Bio", "VII")
    s.getDetails()
except:
    print("Bhai tune galti ki hai constructor me naam nahi daala ya to method me data tune nahi daala")


s1 = student("Kushal")
s1.setDetails("Diploma", "VII")
s1.getDetails()


