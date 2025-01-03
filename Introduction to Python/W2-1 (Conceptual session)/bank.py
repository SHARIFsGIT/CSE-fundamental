from abc import ABC, abstractmethod

class Account(ABC):
    # class property
    accounts = []

    # constructor
    def __init__ (self, name, number, password, type):
        # instance or object properties
        # self refers to the current instance of the class
        # object properties have to accessed with self keyword
        self.name = name
        self.number = number
        self.password = password
        self.balance = 0
        self.type = type

        # access class property with class name
        Account.accounts.append(self)

    def changeInfo(self, new_name):
        self.name = new_name
        print(f'Name has been changed to {new_name}')

    # overriding: method with same name and parameters in parent and child class
    # overloaded method: method with same name but different parameters
    def changeInfo(self, newName, newPassword):
        self.name = newName
        self.password = newPassword

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You have deposited {amount} in your account')

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f'You have withdrawn {amount} from your account')
        else:
            print('Insufficient balance')

    # abstract method: must be implemented in child class
    @abstractmethod
    def showInfo(self):
        pass

# child class of Account (inheritance)
class SavingsAccount(Account):
    def __init__ (self, name, number, password, type, interest_rate):
        super().__init__(name, number, password, type)
        self.interest_rate = interest_rate

    # abstract method implementation in child class
    def showInfo(self):
        print(f'Name: {self.name}, Number: {self.number}, Balance: {self.balance}, Type: {self.type}')


# create an object of the class Account
my_account = Account('John Doe', 123456, '9911', 'savings')

my_account.changeInfo('Nion')