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

    # overloaded method: method with same name but different parameters
    def changeInfo(self, newName = None, newPassword = None):
        if newName:
            self.name = newName
            print(f'Name has been changed to {newName}')
        if newPassword:
            self.password = newPassword
            print('Password has been updated.')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'You have deposited {amount} in your account')

    def withdraw(self, amount):
        if amount > 500 and self.balance >= amount:
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
    def __init__ (self, name, number, password, interest_rate):
        super().__init__(name, number, password, 'savings')
        self.interest_rate = interest_rate

    # abstract method implementation in child class
    def showInfo(self):
        print(f'Account name: {self.name}, Account number: {self.number}, Original balance: {self.balance}, Account type: {self.type}')
    
    def calculateInterest(self):
        interest = self.balance * self.interest_rate / 100
        print(f'Interest: {interest}')
        print(f'Available balance: {self.balance + interest}')


# child class of Account (inheritance)
class StudentAccount(Account):
    def __init__ (self, name, number, password, limit):
        super().__init__(name, number, password, 'student')
        self.limit = limit

    # abstract method implementation in child class
    def showInfo(self):
        print(f'Account name: {self.name}, Account number: {self.number}, Original balance: {self.balance}, Account type: {self.type}')

    # overriding method: same name and parameters in parent and child class
    def withdraw(self, amount):
        if amount > 0 and self.limit >= amount:
            self.balance -= amount
            print(f'You have withdrawn {amount} from your account')
        else:
            print('Insufficient balance')


""" 
# create an object of the class Account
my_account = Account('John Doe', 123456, '9911', 'savings')

my_account.changeInfo('Nion') 
"""


# Create objects of the child classes
my_savings_account = SavingsAccount('John Doe', 123456, '9911', 5)
my_savings_account.deposit(1000)
my_savings_account.calculateInterest()
my_savings_account.showInfo()

my_student_account = StudentAccount('Jane Doe', 654321, '1234', 10000)
my_student_account.deposit(2000)
my_student_account.withdraw(100)
my_student_account.showInfo()