def least_common_multiole(a,b):

    if a > b:
        grater = a
    elif b > a:
        greater = b
    
    while(True):
        if ((greater % a == 0) and (greater % b ==0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("The lcm number is: "+str(least_common_multiole(a,b)))