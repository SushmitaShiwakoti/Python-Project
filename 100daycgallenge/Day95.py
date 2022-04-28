# from timeit import repeat
# from typing import Counter


# # number = [2,4,6,3,6,4,7,8,1,4,3,5,6,7,9,6]
# number=input("Enter the number(as 3,4,5) you should be use comma: ")
# num= number.sort()

# print("The arranging number is: " +str(num) )

# operation =input("choose the operation (mean/median/mode) which you want: ")

# if operation =="mean" :
#     sum_num=sum(number)/len(number)
#     print("\n\nThe average number is:"+ str(sum_num))

# elif operation == "median":
#     median=(len(number)+1)/2
#     print("\n\nThe mesian is:"+ str(median))


# elif operation== "mode":
#     mode=Counter(number)
#     print("The calculating number is mode is: "+ str(mode))

number = input("Enter the number in seperatly: ")
num=int( number.sort())
print(num)

