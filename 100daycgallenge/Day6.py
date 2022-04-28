tuple = ('apple','ball','cat','dog','elephant')
print(len(tuple))
print(tuple[2:5])
print(type(tuple)) 

fruits = ('orange','banana','apple')
y = list(fruits) #converting tuple into list
y.append('cherry') #adding in fruits
y.remove('banana') #removing banana from fruits
# fruits = tuple(y)
print (y) 
(a, b, c) = fruits #unpaking methon
print(a)
print(b)
print(c)
add = tuple+fruits
print(add) #adding the tuple and fruits
for A in fruits: #loop
    print(A)
