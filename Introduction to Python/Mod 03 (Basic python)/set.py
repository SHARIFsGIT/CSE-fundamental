# set: unique items collection
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 5]
print(numbers)

numbers_set = set(numbers)
print(numbers_set)

# list --> []
# tuple --> ()
# set --> {} --> No duplicates

numbers_set.add(11)
print(numbers_set)

# print(numbers_set[2]) # not possible

# numbers_set[2] = 5 # not possible

numbers_set.remove(5)
print(numbers_set)

for item in numbers_set:
    print(item)

if 9 in numbers_set:
    print("9 is in the set")

numbers_set.discard(1)
print(numbers_set)

# Union
a = {1, 2, 5}
b = {1, 3, 4}
print(a & b)
print(a | b)