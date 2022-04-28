
from functools import reduce
import re


list1=[1,3,4,5,6,4,5,67,4,5,8,9]
def greater_num(number):
    return number>5
gr_than_5=list(filter(greater_num,list1))
print(gr_than_5)

list_1=[1,5,6,3,4,7,5,4]
num=reduce(lambda x,y:x*y, list_1)
num=0
for i in list_1:
    num=num+i
    print(num)
print("The number is:",str(num))
