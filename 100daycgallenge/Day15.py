mytuple =("apple","orange","cherry")
myiter= iter(mytuple)
print(next(myiter))
print(next(myiter))

mystr = "Susmita"
A= iter(mystr)
print(next(A))
print(next(A))

class MyNumbers:
      def __iter__(self):
        self.a = 1
        return self

      def __next__(self):
       if self.a <= 10:
        x = self.a
        self.a += 1
        return x
       else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
