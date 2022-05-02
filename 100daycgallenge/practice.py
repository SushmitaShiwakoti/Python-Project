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

# input_string = ("Enter element of list seperatly: ")
# print("\n")
# user_list = input_string.split()
# number = int(input_string).sort()
# print(number)
# print("list: ", user_list)
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])

# print("Sum = ", sum(user_list))

import tkinter as tk
from tkinter import *
from tkinter import ttk

class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Karlos")
        self.button1 = Button( self, text = "CLICK HERE", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )
    def new_window(self):
        self.newWindow = karl2()
class karl2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()
def main(): 
    karl().mainloop()
if __name__ == '__main__':
    main()