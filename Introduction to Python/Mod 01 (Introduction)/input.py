print('This is input file')
input()

input('Give me some money: ')

money = input('Give me the amount: ')
print(f'You gave me {money} dollars.')

friend_money = input('Friend money: ')
family_money = input('Family money: ')
print(friend_money, family_money)
print('Money I got:', friend_money, 'and', family_money)

total = friend_money + family_money
print('Total money:', total)

total_money = int(friend_money) + int(family_money)
print('Total money:', total_money)