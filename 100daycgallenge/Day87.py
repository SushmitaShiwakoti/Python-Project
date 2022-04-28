
from unicodedata import name
print("Check the Citizen, They are able to voting or not:")
print("*_*_*_*_*//_*__*_*_*_*_*_*//_*_*_*_*_*_*_*_\n")

name = input(("Enter your name:"))
age = int(input("Enter your age: "))

if age >= 18:
    print("\n" +name +(", You are allowed for voting for your Leader"))

else:
    print("\n" +name +"You are not allowed for voting for your Leader.")
