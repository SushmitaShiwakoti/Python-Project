import practice
from practice import person1

x=60
def myfunc():
    global y
    y=59
    z=x+y
    def myinnerfunc():
      print("Sumation of x and y is: "+str(z))
    myinnerfunc()
myfunc()
print(x)
print(y)

a=practice.get(" Susmita Shiwakoti, ") #code are save in practice file and we are inherit from there
a=practice.get(" Yasoda Shiwakoti, ")
a=practice.get(" Sabin Shiwakoti, ")

print(person1)








