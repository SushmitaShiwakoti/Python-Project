from asyncio import exceptions


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
c=num1+num2
try:
    print("THe sum of hese two number is:- ",c)
except exceptions as e:
    print(e)

F1=open("sush.txt", "w")
try:
    F=open("duc.txt","w")
except EOFError as e:
    print("print IO error must come",e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    F1.close()
print("This is sush")
print(c)


