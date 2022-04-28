file = open ("myfile.txt","r")
print(file.tell())
print(file.readline())
print(file.tell())

file.seek(10)
print(file.readline())


file.seek(20)
print(file.readline())
file.close