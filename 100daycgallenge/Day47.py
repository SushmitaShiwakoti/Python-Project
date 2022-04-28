def print_msg(msg):
    def printer():
        print(msg)
    return printer

Another= print_msg("Hello i am susmita shiwakoti and today i learning about closures. ")
print(Another())

def make_multiplier(n):
    def multiplier(x):
        return (x*n)
    return multiplier
time3= make_multiplier(3)
time5= make_multiplier(5)

print(time3(5))
print(time5(5))
print(time3(time5(4)))

    
