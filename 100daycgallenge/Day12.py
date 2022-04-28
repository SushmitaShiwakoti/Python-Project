x = lambda a: a+10
print(x(5))

y= lambda a,b:a*b
print(y(5,6))

def myfunc(n):
    return lambda a:a*n
multiply = myfunc(3)
print(multiply(11))

def mynum(n):
    return lambda a:a+n

firstnum = mynum(5)
secondnum = mynum(12)

print(firstnum(55))
print(secondnum(64))
print(type (firstnum))
