name1 = 'Sharif'
name2 = "Sharif"
name3 = """ Shariful
            Islam """
name4 = 'Sharif\'s'

print(name1, name2, name3, name4)

# List --> Mutable or changable
for char in name1:
    print(char)
print(name2[2])

print(name3[2 : 5])
print(name2[-1])
print(name3[ : : -1])

# Not possible to change
""" name2[0] = 'R'
print(name2) """

# Find by condition
if 'r' in name2:
    print('r found')

print(name2.upper())