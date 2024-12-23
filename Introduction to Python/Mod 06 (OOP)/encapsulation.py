# Encapsulation: Hide details
class Bank:
    def __init__(self, holder_name, initital_deposit) -> None:
        # Access Modifiers: Public, Private, Protected
        self.holder_name = holder_name # Public variable
        self.balance = initital_deposit # Public variable
        self.__balance = initital_deposit # Private variable
        self._branch = 'Dhanmondi' # Protected variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return 'Insufficient balance'

user1 = Bank('John', 1000)
print(user1.holder_name)

# user1.balance = 0
# print(user1.balance)

# print(user1.__balance)

# print(user1.get_balance())

user1.deposit(100)
print(user1.get_balance())
print(user1._branch)

print(dir(user1))
print(user1._Bank__balance)