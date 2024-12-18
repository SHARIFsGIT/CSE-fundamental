n = input()
array = list(map(int, input().split()))

flag = True
operations = 0

while flag is True:
    for i, num in enumerate(array):
        if num % 2 == 1:
            flag = False
            break
        else:
            array[i] /= 2
    if flag:
        operations += 1
print(operations)