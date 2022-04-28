from email.mime import base


base = int(input('Enter the base number: '))
exponent = int(input('Enter the exponent number: '))
# base = 4
# exponent = 5
result = 1

while exponent != 0:
    result *= base
    exponent -=1

print("Your answer is: "+ str(result))