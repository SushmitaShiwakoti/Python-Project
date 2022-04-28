num= -1
def search (list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals() ['num']=i
            return True
        i=i+1
    return False
list=[4,5,6,7,3,8,6,9]
n=8
if search(list,n):
        print('Found at',num)
else:
        print('Not found')