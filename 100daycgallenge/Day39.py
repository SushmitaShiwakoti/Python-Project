import email
class Student:
    def __init__(self,fname, lname) -> None:
        self.name= fname
        self.lname= lname

    def explain(self):
        return f"This is student {self.name} {self.lname}"

    @property
    def email(self):
        if self.name==None or self.lname==None:
            return "Email is not set. please set it using setter"
        return f"{self.name}.{self.lname}"

    @email.setter
    def email(self, string):
        print("seting now..")
        name=string.split("@") [0]
        self.name=name.split(".") [0]
        self.lname= name.split("." [3])

    @email.deleter
    def email(self):
        self.name=None
        self.lname=None
Nepali_supporter = Student("Nepali", "Supporter")
print(Nepali_supporter.email)
Nepali_supporter.name="US"
print(Nepali_supporter.email)

del Nepali_supporter.email
print(Nepali_supporter.email)
# Nepali_supporter.email="susmita.shiwakoti@s.com"
# print(Nepali_supporter.email)