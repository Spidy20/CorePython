from sklearn.linear_model  import LinearRegression

#inheritance
class Person():

  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def __init__(self, fname, lname,mname):
        self.firstname = fname
        self.lastname = lname

  def printname(self):
     print(self.firstname, self.lastname)

x = Person("kushal","Bhavsar")
x.printname()