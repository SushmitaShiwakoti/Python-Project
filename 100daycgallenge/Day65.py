from time import time
start = time()

email = input('Enter your Email: ')
email = email.strip()
slicer_index = email.index("@")
username = email[:slicer_index]
domain_name = email[slicer_index+1:]
print('Your Username is ', username, 'and your domain is', domain_name)

end = time()
execution_time = end - start
print('Execution Time (s): ', execution_time)
print('susmiita shiwakoti, thank you')