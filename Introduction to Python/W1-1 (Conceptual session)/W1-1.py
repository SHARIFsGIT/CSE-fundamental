# There is no charecter type in python. They have string type only.

# Float division
from numpy import square


result = 10 / 6
print(result)

# Integer division
result = 10 // 6
print(result)

# Power operation
result = 2 ** 5
print(result)

# String operation
name = 'string'
for char in name:
    print(char) # but comes with new line

name = 'string'
for char in name:
    print(char, end=" ") # comes with space, new line removed

print()

name = 'string'
for char in name:
    print(char, end="") # space removed, new line removed

print()
 
# Getting index
for i in range(5):
    print(i)

for i in range(len(name)):
    print(name[i])
    
# Getting index and value
for i, char in enumerate(name):
    print(f"index: {i} value: {char}")

# Unpacking
a, b = [10, 20]
print(a)
print(b)

# Tuples unpacking
for en in enumerate(name):
    print(en)
    
# Condition
a = 50
b = 0

if a > b and b != 0:
    print("a is greater")
elif a == 0:
    print("a is zero")
elif b == 0:
    print("b is zero")
else:
    print("a is less")
    
# Function (with return)
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Function (without return)
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result)

# Argument parameter
def result_calculate(name, *args):
    print(name, args)
result_calculate('Mr. X', 75, 90, 75, 87) # Comes with tuples

def result_calculate(name, *args):
    sum = 0
    for num in args:
        sum += num
    print(f"Name: {name}, Result: {sum}")
result_calculate('Mr. X', 75, 90, 75, 87)

def result_calculate(name, *args):
    sum = 0
    for num in args:
        sum += num
    return name, sum # return multiple values & comes as tuple
result = result_calculate('Mr. X', 75, 90, 75, 87)
print(result)

def result_calculate(name, *args):
    sum = 0
    for num in args:
        sum += num
    return [name, sum] # return multiple values & comes as list
result = result_calculate('Mr. X', 75, 90, 75, 87)
print(result)

def result_calculate(name, *args):
    sum = 0
    for num in args:
        sum += num
    return [name, sum] # return multiple values & comes as list
name, mark = result_calculate('Mr. X', 75, 90, 75, 87) # unpacking
print(f"Name: {name}, Result: {mark}")

# Scope
x = 10
def fun():
    x = 20
    print("Inside fun: ", x)
fun()
print("Outside fun: ", x)

# Scope: If I want to overwrite global variable
x = 10
def fun():
    global x
    x = 20
    print("Inside fun: ", x)
fun()
print("Outside fun: ", x)

# List comprehension
nums = [1, 2, 3, 4, 5, 6]
for i in range(len(nums)):
    nums[i] = nums[i] ** 2
print(nums)

# Read only
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    num = num ** 2
print(nums)

square_nums = [num ** 2 for num in nums]
print(square_nums)

# Loop way
odd_list = []
for num in nums:
    if num % 2 != 0:
        odd_list.append(num)
print(odd_list)

# List comprehension way
odd_list = [num for num in nums if num % 2 != 0]
print(odd_list)

# Input in python
n = input('Enter a number: ')
print(n)
print(type(n))

# Type cast
n = input('Enter a number: ')
n = int(n)
print(n)
print(type(n))

# Type cast
n = int(input('Enter a number: '))
print(n)
print(type(n))

# Array input
n = int(input('Enter array size: '))
arr = input('Enter array elements: ')
print(n)
print(arr)

# Array input like C (but error in array input in same line like contest cause it takes whole lines in string format)
nums = []
n = int(input())
for i in range(n):
    x = int(input())
    nums.append(x)
print(n)
print(nums)

# To solve above error
# Way 01: but it gives string type
n = int(input())
arr = input()
print(arr)
print(type(arr))

# Way 01: solving string type but comes with list and each value is a string
n = int(input())
arr = input().split()
print(arr)
print(type(arr))

# Final solve
n = int(input())
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(arr)
print(type(arr))

# Way 02 with list comparison
n = int(input())
arr = input().split()
int_arr = [int(x) for x in arr]
print(int_arr)
print(type(int_arr))

# Map(different from C++)
def square(x):
    return x * x
nums = [1, 2, 3, 4]
square_nums = map(square, nums) # it gives us objects
print(square_nums)

# Map: object to list
def square(x):
    return x * x
nums = [1, 2, 3, 4]
square_nums = list(map(square, nums))
print(square_nums)

# Way 03: array input using map(with custom made function)
arr = input().split()
def convert_int(x):
    return int(x)
int_array = list(map(convert_int, arr))
print(int_array)
print(type(int_array))

# Way 03: array input using map(with buildin function)
arr = input().split()
def convert_int(x):
    return int(x)
int_array = list(map(int, arr))
print(int_array)
print(type(int_array))

# Array input in one line
arr = list(map(int, input().split()))
print(arr)