def multiple():
    return 3, 4
print(multiple())

things = 'pen', 'bottle', 'book'
print(things)
print(type(things))

print(things[0])
print(things[-1])
print(things[1 : 3])
print(things[1 : 2])
print(things[1 : 1])

if 'pen' in things:
    print('pen is in the list')

for item in things:
    print(item)

""" things[0] = 'phone'
print(things[0])
 """
print(len(things))

# Tuple is unchangeable but list is changeable
mega = ([1, 2, 3], [4, 5])
mega[0] = [6] # not possible
print(mega)

mega[0][1] = 6
print(mega)