from xml.dom.minidom import NamedNodeMap

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)

class Student(Person):
    def __init__(self, roll, name, age, phone):
        self.roll = roll
        Person.__init__(self, name, age)
        self.phone = phone

    def display(self):
        print("Roll-no.: ", self.roll)
        Person.display(self)
        print("Phone: ", self.phone)

s1 = Student(1, 'Susmita', 20, 980736832)
print('Student Detail.....')
s1.display()

        
