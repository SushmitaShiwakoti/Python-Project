class program:
    x=5*98
print(program.x)

class myclass:
    x = 10
obj = myclass()
print(obj.x)



class person:
    def __init__(myprogram,name,age,address,number):
        myprogram.name=name
        myprogram.age=age
        myprogram.addrress=address
        myprogram.number =number
objc =person("susmita shiwakoti",40, 'kathmandu',9748588585)
print("Myname is:- "+objc.name )
print("I live in:- "+objc.addrress)
print("Contact no.:- "+ str(objc.number))
print("My age is:- "+str(objc.age)) 


class program:
    def __init__(myprogram,name,age):
        myprogram.name=name
        myprogram.age=age
      
    def myfun(objc):
       print("myname is:-"+objc.name  +"and age is:-"+str(objc.age))

obb =program("yasoda shiwakoti",20)
obb.myfun()

