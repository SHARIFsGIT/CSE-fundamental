test = int(input()) 

for t in range(test):
    elements = int(input())
    array = list(map(int, input().split()))
    
    count = elements

    for i in range(elements):
        for j in range(i + 1, elements):
            if array[j] <= array[j - 1]:
                break
            count += 1
    print(count)
