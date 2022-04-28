
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def print(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Susmita", "Shiwakoti", 2022)
x.print()
x = Student("yasoda", "Shiwakoti", 2022)
x.print()
x = Student("sabin", "Shiwakoti", 2022)
x.print()


