n = input()
array = list(map(int, input().split()))

freq = {}

for num in array:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

remove = 0

for key, value in freq.items():
    if(value > key):
        remove += value - key
    elif(value < key): 
        remove += value   
print(remove)