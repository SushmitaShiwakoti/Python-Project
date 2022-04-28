from fileinput import close

with open("myfile.txt") as file:
    A= file.read(10)
    print(A)
    A = file.readline()
    print(A)
    A= file.seek(5)
    print(file.readline())

f =open("practicefile.txt","r")
print(f.read())
# f.write("today i learn about open with file") we only used one of create/read/write/append mode at a time
f.close()

