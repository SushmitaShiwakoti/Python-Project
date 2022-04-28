import pickle
# cars= ['audi','BMW','maruti','Harryti']
# file='mycar.pkl'
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()


file='mycar.pkl'
fileobj=open(file, 'rb')
mycars=pickle.load(fileobj)
print(mycars)
print(type(mycars))
