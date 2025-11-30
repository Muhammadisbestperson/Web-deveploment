from abc import ABC,abstractmethod 
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can move and run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Dog(Animal):
    def move(self):
        print("I can bark")
class Lion(Animal):
    def move(self):
        print("I can Roar")

R=Human()
R.move()

K= Snake()
K.move()

R=Dog()
R.move()

K=Lion()
K.move()