n, q = map(int, input().split())
array = list(map(int, input().split()))

total = [0]
for i in array:
    total.append(total[-1] + i)

for query in range(q):
    l, r = map(int, input().split())
    print(total[r] - total[l - 1])