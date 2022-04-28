my_str = 'aItebGjstU'

my_str =my_str.casefold()

rev_str= reversed(my_str)


if list(my_str)== list(rev_str):
    print("the string is pLindrome.")

else:
    print("The string is not a polidrome.")