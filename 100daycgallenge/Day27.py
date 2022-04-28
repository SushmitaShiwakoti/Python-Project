def sq(a):
    return a*a

num=[2,4,56,3,45,4,6,77,5,4]
square=list(map(sq, num))
print (square)

squ= list(map(lambda x:x*x+3,num))
print(squ)

def squre(a):
    return a*a
def cube(a):
    return a*a*a
fun =[squre, cube]
# number=[3,56,78,7,8,9]
for i in range(5):
    val=list(map(lambda x:x(i),fun))
    print(val)