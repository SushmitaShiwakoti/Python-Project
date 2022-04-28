class Employee:
    no_of_level = 10

    def __init__(self, name, salary, role) :
        self.fullname=name
        self.salary = salary
        self.role=role

    def printdetail(self):
        return f"The name is {self.name}. Salary is {self.salary} and role is aaaaaaa{self.role}"

    def change_leaves(cls, newleaves):
        cls.no_of_leaves =newleaves

    def from_dash(cls, string):
        return cls(*string.split("-"))

    def print_good(string):
        print ("this is good"+string)

susmita = Employee("susmita", 255, 'Instructor')
# kopila = Employee.from_dash("kopila-345-student")
sarita = Employee("sarita",287, 'student')

print(susmita.printdetail)
# Employee.printgood("kopila")
print(sarita.fullname)       