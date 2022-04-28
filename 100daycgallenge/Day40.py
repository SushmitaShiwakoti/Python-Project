class student:
    def __init__(self, fname, lname):
        self.fname= fname
        self.lname= lname

    def explain(self):
        return f"This student is {self.fname} {self.lname}"
    
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithsusmita.com"

    # @email.setter
    # def email(self, string):
    #     print("Setting now....")
    #     name=string.split("0") [0]
    #     self.fname=name.split(".") [0]
    #     self.lname=name.split (".") [1]

    email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skill=student ("susmita", "shiwakoti")
print(skill.explain())
print(skill.email())
# print(dir(skill))
import inspect
print(inspect.getmembers(skill))