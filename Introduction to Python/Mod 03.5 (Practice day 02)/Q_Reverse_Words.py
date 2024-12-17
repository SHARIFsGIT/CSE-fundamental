s = input()
temp = []

for word in s.split(' '):
    temp.append(word[ : : -1])
print(' '.join(temp))