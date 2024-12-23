# Base/Parent class and Derived/Child class
class Device:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running device: {self.brand}'

class Laptop:
    def __init__(self, memory, SSD) -> None:
        self.memory = memory
        self.SSD = SSD
    
    def coding(self):
        return f'Learning Python and practice'
    
class Phone(Device):
    def __init__(self, brand, price, color, origin, duel_sim) -> None:
        self.duel_sim = duel_sim
        super().__init__(brand, price, color, origin)

    def run(self):
        return f'Phone browing'

    def phone_call(self, number, text):
        return f'Sending SMS to {number} with {text}'
    
    def __repr__(self) -> str:
        return f'Phone: {self.brand} {self.price} {self.duel_sim}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass

my_phone = Phone('Samsung', 12000, 'Black', 'Korea', True)
my_phone.phone_call(123456789, 'Hello')
print(my_phone.brand)
print(my_phone)

print(issubclass(Phone, Device))
print(isinstance(my_phone, Phone))
print(isinstance(my_phone, Device))