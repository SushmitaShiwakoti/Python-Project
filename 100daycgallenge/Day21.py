from re import T


price =200
txt = "The price of my food is {} dollars."
print(txt.format(price))
q=3
p=34
T=30
order="I want {} pieces of item number {} for{:.2f} dollars."
print(order.format(q,p,T))
order="I want {2} pieces of item number {0} for{1} dollars."
print(order.format(q,p,T))
age=20
name='susmita shiwakoti'
details= "Her name is {1} and {1} is {0} year old."
print(details.format(name,age))
