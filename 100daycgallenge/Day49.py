from logging import exception


a= input("what is your name: ")
if a.isnumeric():
    raise Exception("number is not allowed")
print(f"hello {a}")
b=input("How much do you earn:")
if int (b)==20:
    raise ZeroDivisionError("b is stopping the process")
print("Your salary is: " +str(b))

c= input("enter your second name:")
try:
    print(a)
except exception as e:
    if c=='sush':
        raise ValueError("sush is block")
print("exception handle")