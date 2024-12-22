class Calculator:
    brand = 'Casio MS990'

    def addition(self, num1, num2):
        return num1 + num2
    
    def subtraction(self, num1, num2):
        return num1 - num2
    
    def multiplication(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return 'Division by zero is not allowed.'

calc = Calculator()

print(f'Welcome to {calc.brand} - Calculator!')
print(f'----------------------------------')

print('Choose an operation: ')
print('   1. Addition (+)')
print('   2. Subtraction (-)')
print('   3. Multiplication (*)')
print('   4. Division (/)')
print(f'----------------------------------')

try:
    operation = int(input('Enter your choice (1-4): '))

    if operation == 1:
        print('You choose for addition operation.')
    elif operation == 2:
        print('You choose for subtraction operation.')
    elif operation == 3:
        print('You choose for multiplication operation.')
    elif operation == 4:
        print('You choose for division operation.')

    if operation not in [1, 2, 3, 4]:
        print('Invalid choice. Please try again.')
    else:
        print(f'----------------------------------')
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        print(f'----------------------------------')

        if operation == 1:
            print(f'Addition result: {calc.addition(num1, num2)}')
        elif operation == 2:
            print(f'Subtraction result: {calc.subtraction(num1, num2)}')
        elif operation == 3:
            print(f'Multiplication result: {calc.multiplication(num1, num2)}')
        elif operation == 4:
            print(f'Division result: {calc.division(num1, num2)}')

except ValueError:
    print('Invalid input. Please enter numbers only.')