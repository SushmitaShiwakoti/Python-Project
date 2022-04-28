A = 22
B = 11
i = 1
if A>B:
    print("A is greater than B")
elif A==B:
    print("A is not equal to B")    
C = 24
if A>B and A<C: print("Both condition is true")
if A>B or A>C: print("At least one condition is true")

while i<6:          # this is while loop
    i+=1
    if i==4:
        break
    print(i)
    
fruits = ['apple','banana','orange']
for x in fruits:         # this is for loop
    print(x)
    if x == 'banana':
        break

for x in range(3,20,3): print(x)
    