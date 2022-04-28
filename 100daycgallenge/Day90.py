a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    print("The divided number is: "+str(a/b))
except Exception:
    print("Hey, You can't divide a number by zero.")

finally:
    print("Resource close")

