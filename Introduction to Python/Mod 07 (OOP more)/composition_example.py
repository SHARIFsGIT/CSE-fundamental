class Processor:
    def __init__(self, brand, cores, speed):
        self.brand = brand
        self.cores = cores
        self.speed = speed 

    def get_specs(self):
        return f"{self.brand} Processor with {self.cores} cores at {self.speed} GHz"


class Memory:
    def __init__(self, capacity):
        self.capacity = capacity  # in GB

    def get_specs(self):
        return f"{self.capacity} GB RAM"


class Storage:
    def __init__(self, type_, capacity):
        self.type = type_  # SSD or HDD
        self.capacity = capacity  # in GB or TB

    def get_specs(self):
        return f"{self.capacity} {self.type} Storage"


class Computer:
    def __init__(self, processor, memory, storage):
        self.processor = processor
        self.memory = memory
        self.storage = storage

    def get_specs(self):
        return (
            f"Computer Specifications:\n"
            f"  - {self.processor.get_specs()}\n"
            f"  - {self.memory.get_specs()}\n"
            f"  - {self.storage.get_specs()}"
        )


# Creating components
processor = Processor(brand="Intel", cores=8, speed=3.6)
memory = Memory(capacity=16)
storage = Storage(type_="SSD", capacity="1TB")

# Creating a computer with components
computer = Computer(processor=processor, memory=memory, storage=storage)

# Displaying the computer's specifications
print(computer.get_specs()) 