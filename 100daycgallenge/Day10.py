def  my_name(fname,lname):
    print(fname," "+lname)
print("My family memeber are:")
my_name("Dhurba","Shiwakoti")
my_name("Sarita","Shiwakoti")
my_name("Susmita","Shiwakoti")
my_name("Kopila", "Shiwakoti")
my_name("Sabin","Shiwakoti")

def my_function(*fruits):
    print("The fruits name is:" +fruits[3])
my_function("Apple","Orange","Banana","Cherry")

def child(child1, child2, child3):
    print("The youngees child of my family is:"+child3)
child(child1="sush", child2="yaso", child3="sabi") #key = value syntax
def function(food):
    for x in food:
        print(x)
fruits =["apple","banana","orange","mango"]
function(fruits)
def number(x):
    return 5 * x
print(number(3))
print(number(10))
print(number(13))

# def tri_recursion(k):
#     if(k>0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#         return result
# print('RECURSION EXAMPLE RESULT IS:')
# tri_recursion(6)

