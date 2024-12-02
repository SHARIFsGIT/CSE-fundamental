numbers = [10, 11, 12, 13, 14, 15]
sum = 0
for number in numbers:
    sum += number
    if number % 2 == 0:
        print(number, 'is even')
    else:
        print(number, 'is odd')
print(f"Sum of numbers:", sum)


text = 'Shadow numbers'
for char in text:
    print(char)


for i in range(1, 10, 2):
    print(i)


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Value: {fruit}")
