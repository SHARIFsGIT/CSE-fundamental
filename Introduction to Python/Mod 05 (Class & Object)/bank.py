class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000000

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}. New balance: {self.balance}')
        else:
            print('Invalid deposit amount')
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You cannot withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'You can not withdraw above bank max limit {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'You withdraw {amount}. Current balance: {self.get_balance()}')

my_bank = Bank(15000)
my_bank.withdraw(25)
my_bank.withdraw(500)

my_bank.deposit(5000)
print(my_bank.get_balance())