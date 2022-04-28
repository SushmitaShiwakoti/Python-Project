cars = ['Ford','Volvo','BMW']
x = cars[0]
print(x)
cars=['Toyata']
print(cars)

x=len(cars)
print(x)
for x in cars:
    print(x)
cars.append('Hond')
print(cars)
cars.pop(1)
print(cars)
fruits = ['apple','banana','cherry','orange','mango']
fruits.sort()
print(fruits)
fruits.remove('banana')
print(fruits)
x=cars.extend(fruits)
print(x)

