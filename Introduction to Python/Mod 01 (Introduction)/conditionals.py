num1 = input('Enter number 1: ')
num2 = input('Enter number 2: ')

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 == num2:
    print(f"{num1} and {num2} are equal")
else:
    print(f"{num2} is greater than {num1}")

boss = False
if boss is True:
    print("You are the boss")
else:
    print("You are not the boss")

if boss is not True:
    print("You are not the boss")
else:
    print("You are the boss")

# Nested condition
coin = 'head'
if boss == True:
    print("You are the boss")
    if coin == 'tail':
        print("You lost the game")
    else:
        print("You won the game")
else:
    print("You are not the boss")