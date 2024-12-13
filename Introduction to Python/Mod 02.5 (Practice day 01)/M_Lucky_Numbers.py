a, b = map(int, input().split())

def is_lucky(num):
    for digit in str(num):
        if digit not in {'4', '7'}:
            return False
    return True

lucky_numbers = []
for num in range(a, b + 1):
    if is_lucky(num):
        lucky_numbers.append(num)

if lucky_numbers:
    print(' '.join(map(str, lucky_numbers)))
else:
    print('-1')