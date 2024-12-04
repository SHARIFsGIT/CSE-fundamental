def full_name(first, last):
    name = f'Full name: {first} {last}'
    return name
# name = full_name('Shariful', 'Islam')
name = full_name(first = 'shariful', last = 'islam')
print(name)


def famous_name(first, last, *title):
    name = f'{first} {last}'
    return name
name = famous_name(first = 'shariful', last = 'islam')
print(name)


def famous_name(first, last, **addition):
    name = f'{first} {last}'
    print(addition)
    print(addition['author'])
    for key, value in addition.items():
        print(f'{key}: {value}')
    return name
name = famous_name(first = 'shariful', last = 'islam', title = 'student', author = 'Nitush')
print(name)


def a_lot(n1, n2):
    sum = n1 + n2
    multiplies = n1 * n2
    remainder = n1 - n2
    return sum, multiplies, remainder # return as tupple
    return [sum, multiplies, remainder] # return as list
result = a_lot(10, 5)
print(result)