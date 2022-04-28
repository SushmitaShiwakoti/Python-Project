def getNUm(x):
    for i in range(x):
        yield i

seq= getNUm(3)
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())

def gen(n):
    for i in range(n):
        yield i

g=gen(5)
print("New generator number is:- "+ str(g.__next__()))
print("New generator number is:- " + str(g.__next__()))
print("New generator number is:- " + str(g.__next__()))

h= "3564547"
ier =iter(h)
print("this is iter number: "+str( ier.__next__()))
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

for c in h:
    print(c)