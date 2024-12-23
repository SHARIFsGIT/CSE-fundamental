from abc import ABC, abstractmethod
# abc is Abstract Base Class

class Animal(ABC):
    @abstractmethod # decorator: enforce the child class to implement this method
    def eat(self):
        print('Eating')

    @abstractmethod
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print(f'{self.category} {self.name} is eating banana')

    def move(self):
        print(f'{self.category} {self.name} is jumping')

lyca = Monkey('Lyca')
lyca.eat()
lyca.move()