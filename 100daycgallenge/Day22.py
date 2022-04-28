file=open("practicefile.txt","r")

print(file.read(5))
# print(file.read())
print(file.readline())

for x in file:
    print(x)

# file=("practicefile.txt","a")
# file.write("Thank you so much everyone for supporting")
# file.close()
# file=open("practicefile.txt","r")
# print(file.read())

f= open("demofile3.txt", "w")
f.write("Thank you so much to everyone.")
f.close()

f = open("demofile3.txt", "r")
print(f.read())
f = open ("myfile.txt", "x")
