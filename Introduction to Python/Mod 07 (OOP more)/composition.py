class Engine:
    def __init__(self) -> None:
        pass

    def start(self):
        return 'Engine started'
    

class Driver:
    def __init__(self) -> None:
        pass


class Car:
    def __init__(self) -> None:
        # Creating an object of the Engine class
        self.engine = Engine()
        # Creating an object of the Driver class
        self.driver = Driver()
    
    def start(self):
        # Delegating the start action to the Engine class
        return self.engine.start()
    
# composition provides has-a relationship