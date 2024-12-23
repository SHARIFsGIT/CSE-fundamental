class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'Vehicle: {self.name} {self.price}'

    def move(self):
        return f'Running vehicle: {self.name}'

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self) -> str:
        return f'Bus: {self.name} {self.price} {self.seat}'

class Truck(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class Pickup(Truck):
    def __init__(self, name, price, weight, size) -> None:
        self.size = size
        super().__init__(name, price, weight)

class AC_bus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'AC Bus: {self.seat} {self.temperature}')
        return super().__repr__()

green_line = AC_bus('Green Line', 1000000, 50, 20)
print(green_line)