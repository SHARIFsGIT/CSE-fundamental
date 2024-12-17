n = int(input())
array = list(map(int, input().split()))

min_index = array.index(min(array))
max_index = array.index(max(array))

array[min_index], array[max_index] = array[max_index], array[min_index]

print(*array)