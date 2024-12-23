class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counters = []
        self.managers = []
        self.supervisors = []
        self.fare = []

class Driver:
    def __init__(self, name, license, age) -> None:
        self.license = license
        self.name = name
        self.age = age

class Counter:
    def __init__(self) -> None:
        pass

    def purchase(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

driver = Driver('Shariful', 'S520H', 25)