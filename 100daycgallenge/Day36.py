class Employee:
    no_of_leavwes =8

    def __init__(self,aname, asalary, arole) -> None:
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetail (self):
        return f"the name is {self.name}.salary is {self.salary} and role is {self.role}."
    
    @classmethod
    def change_leaves(cls, new_leaves):
        cls_no_of_leaves=new_leaves

    def _add_(self, other):
        return self.salary + other.salary

    def _truedive_(self,other):
        return self.salary/other.salary
    
    def __repr__(self):
        return f"the name is {self.name}. salary is {self.salary} and {self.role}"
    
emp1=Employee("susmita", 546, "programmer")
emp2=Employee("sush", 746, "programmer")
print(emp2)
print(emp1)