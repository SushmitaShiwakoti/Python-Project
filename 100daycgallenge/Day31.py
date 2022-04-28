from imp import init_builtin
from types import ClassMethodDescriptorType

class Employee:
    no_of_leaves=67
    var=37
    def __init__(self, name, salary, role) :
        self.fname= name
        self.salary =salary
        self.role = role
    
    def printdetail(self):
        return f"the name is {self.name}. salary is {self.salary} and role is {self.role}."

    @classmethod
    def change_level(cls, newleaves):
        cls.no_of_level=newleaves

    # @classmethod
    # def from_dash(cls, string):
    #     cls(*string.split("_"))
sush=Employee("susmits", 2456, "programmer")
yaso=Employee("susmits", 2456, "programmer")
yaso.change_level(34)
print(sush.no_of_leaves)
print(yaso.var)
print(sush)

