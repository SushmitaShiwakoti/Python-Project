username= input("Enter your name: ")
print("Your name is: "+ username)

try:
    print(x)
except:
    print("An exception occured")
finally:
    print("The 'try except' is finished")
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
    print("Hello")
except:
    print("somthing went wrong")
else:
    print("Nothing went wrong")