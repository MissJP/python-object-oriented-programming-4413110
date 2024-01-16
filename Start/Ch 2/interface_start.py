# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod

#interface, all classes will have to implement abstractmethods
class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):

    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"

c = Circle(10)
print(c.calcArea())
print(c.toJSON())
