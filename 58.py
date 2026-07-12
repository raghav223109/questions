from abc import ABC , abstractmethod

class  shape(ABC):
    @abstractmethod

    def area(self):
        pass

class circle(shape):
    def area(self):
        return 3.14 * 5 * 5

c = circle()
print(c.area())