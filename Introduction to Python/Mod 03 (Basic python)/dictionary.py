person = {'name': 'John', 'address': 'bremen', 'age': 23, 'job': 'banker'}
print(person)
print(person['age'])
print(person.values())

person['country'] = 'Germany' 
print(person)

person['address'] = 'Munich'
print(person)

del person['age']
print(person)

# For getting keys
for item in person:
    print(item)

# For getting keys and values
for key, value in person.items():
    print(key, value)

# List index
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 5]
for index, number in enumerate(numbers):
    print(index, number)