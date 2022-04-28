set1 = {"susmita","sarita","kopila","priti","priya"}
set2 = {"sarita","Dhurba","sabin","priya"}

print(type(set1))
print(set1)
set3=set1.symmetric_difference(set2)
print(set3)
set1.update(set2)
print(set1)
set1.pop()
print(set1)
set2.intersection_update(set1)
print(set2)
set2.remove("priya")
print(set2)
x =set1.symmetric_difference(set2)
print(x)
for y in set1:
    print(y)
