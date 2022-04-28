# def get(name):
#     print("Hello" +name +"How can i help you")

# person1={
#     "name":"Susmita shiwakoti",
#     "age":20,
#     "country":"Nepal"
# }

#//////
# numbers= range(3)
# output=numbers
# print(output)

#//////
# from calendar import*
# year = int(input('Enter Year: '))
# print(calendar(year, 2, 1, 8, 4))

#////////////
# from time import time
# start = time()

# email = input('Enter your Email: ')
# email = email.strip()
# slicer_index = email.index("@")
# username = email[:slicer_index]
# domain_name = email[slicer_index+1:]
# print('Your Username is ', username, 'and your domain is', domain_name)

# end = time()
# execution_time = end - start
# print('Execution Time (s): ', execution_time)

#//////////////////////
# FirstOperand = input('Enter First Operand(Any Numeric value\n')

# d = {}
# d[None] = 'This is bit tricky!'
# print(d)

# i

# import turtle

# T=turtle.Turtle()
# T.color('red')
# T.speed(200)
# T.left(90)
# T.backward(10)
# T.pensize(5)
# T.shape('turtle')

# def tree(i):
#     if i <10:
#         return
#     else:
#         T.forward(i)
#         T.color('green')
#         T.circle(3)
#         T.color('red')
#         T.left(30)
#         tree(3*i/4)
#         T.right(60)
#         tree(4*i/4)
#         T.left(30)
#         T.backward(i)


# tree(100)
# turtle.done()


# a

input_string = ("Enter element of list seperatly: ")
print("\n")
user_list = input_string.split()
number = int(input_string).sort()
print(number)
print("list: ", user_list)
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

print("Sum = ", sum(user_list))