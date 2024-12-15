def double(x):
    return x * 2
result = double(4)
print(result)

doubled = lambda x : x * 2
result = double(4)
print(result)

add = lambda x, y : x + y
result = add(3, 5)
print(result)

# map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))

numbers = [10, 13, 44, 65]
doubled_numbers = map(lambda x: x*2, numbers)
print(list(doubled_numbers))

# list of dictionaries with lambda
actors = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 28},
    {"name": "Bob", "age": 35}
]
juniors = filter(lambda actor : actor["age"] > 30, actors)
fivers = filter(lambda actor : actor["age"] % 5 == 0, actors)
print(list(juniors))
print(list(fivers))