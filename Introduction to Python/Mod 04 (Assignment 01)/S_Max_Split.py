string = input()

l = r = 0
i = j = 0

result = []

for char in string:
    if (char == 'L'):
        l += 1
    else:
        r += 1
    
    j += 1
    
    if (l == r):
        result.append(string[i : j])
        i = j
        l = r = 0

print(len(result))

for substring in result:
        print(substring)