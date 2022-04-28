# count Number of digits in an integer using while loop

num = 2345
count = 0

while num != 0:
    num//=10
    count +=1

print('Number of digit: '+ str(count))

#using inbuilt method
num = 12367
print(len(str(num)))