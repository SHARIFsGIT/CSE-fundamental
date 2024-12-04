def sum(num1, num2, num3 = 0):
    result = num1 + num2 + num3
    return result
total = sum(99, 11, 5)
print('total:', total)

# args:
def all_sum(*numbers):
    print(numbers)
    for num in numbers:
        print(num)
total_num = all_sum(45, 56, 30)
print('All sum:', total_num)

def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum
total_num = all_sum(45, 56, 30, 40)
print('All sum:', total_num)