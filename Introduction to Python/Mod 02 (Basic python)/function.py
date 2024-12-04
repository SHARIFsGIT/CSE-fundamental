def double_it(num):
    result = num * 2
    print('Inside the function.py file', result)
    return result
double_it(5)

def add_numbers(num1, num2):
    result = num1 + num2
    return result
total = add_numbers(10, 50)
print(total)

final = double_it(total)