# Break:
num = 1
while num < 10:
    print(num)
    num += 1
    if num == 5:
        break

# Continue:
num = 0
while num < 10:
    num += 1
    if num % 2 == 1:
        continue
    print(num)