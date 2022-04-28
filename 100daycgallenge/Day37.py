from abc import ABC, abstractmethod
class shape (ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(shape):
    type= "Rectangle"
    side= 4
    def __init__(self) -> None:
        self.length= 6
        self.breadth= 7
        self.l=78
        self.b=56

    def printarea(self):
        return self.length*self.breadth
    def addition(self):
        return self.l+self.b

rect1= Rectangle()
print(rect1.printarea())
print(rect1.addition())