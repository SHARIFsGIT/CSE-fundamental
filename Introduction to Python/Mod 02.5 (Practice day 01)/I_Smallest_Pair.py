test_case = int(input())

for tc in range(test_case):
    n = int(input())
    array = list(map(int, input().split()))

    result = []
    for i in range(n):
        for j in range(i+1, n):
            result.append(array[i] + array[j] + (j - i))
    print(min(result))