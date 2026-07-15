from abc import ABC

class Animal(ABC):
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

        
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

print("program ended here")