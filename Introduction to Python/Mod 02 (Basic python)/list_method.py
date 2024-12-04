num = [1, 2, 30, 4, 4, 1, 5, 6, 7, 8, 9]
num.append(10)
print(f'Append:', num)

num.insert(3, 15)
print(f'Insert:', num)

if 15 in num:
    num.remove(15)
print(f'Remove:', num)

num.pop(3)
print(f'Pop 3rd index:', num)

last = num.pop()
print(f'Last by pop:', last)
print(f'Numbers after pop:', num)

num.sort()
print(f'Sort:', num)

num.reverse()
print(f'Reverse:', num)

if 1 in num:
    index = num.index(1)
    print(f'Index:', index)

if 100 in num:
    index = num.index(1)
    print(f'Index:', index)

appears = num.count(1)
print(f'Count:', appears)

num.extend([10, 20])
print(f'Extend:', num)

num.clear()
print(f'Clear:', num)