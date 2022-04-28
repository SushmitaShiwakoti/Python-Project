#program to check if a string is palindrome or not
my_str1 ='arCHtEcTurE'
my_str2 ='AtfyRGdDgrYFTa'

# make it suitable for caseless comparison
my_str1 = my_str1.casefold()
my_str2 = my_str2.casefold()

#reverse the string
rev_str1= reversed(my_str1)
rev_str2= reversed(my_str2)
# check if the string is equal to its reverse
if list(my_str1) == list(rev_str1):
    print('The string is a palindrome.')

else:
    print('The string is not a palindrome.')

if list(my_str2) == list(rev_str2):
    print('The string is a palindrome.')

else:
    print('The string is not a palindrome.')