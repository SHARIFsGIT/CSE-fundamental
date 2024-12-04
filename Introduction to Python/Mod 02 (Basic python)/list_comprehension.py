num = [40, 50, 60, 41, 7, 15, 70, 80, 71, 82]
odds = []
for n in num:
    if n % 2 == 1 and n % 5 == 0:
        odds.append(n)
print(odds)

odd_num =[n for n in num]
print(odd_num)

odd_nums =[n for n in num if n % 2 == 1 and n % 5 == 0]
print(odd_nums)

players = ['player1', 'player2', 'player3']
ages = [25, 22, 20]

age_comb = []
for player in players:
    print('Player:', player)
    for age in ages:
        print(player + ':', age)
        age_comb.append([player, age])
print(age_comb)

comb = [[player, age] for player in players for age in ages]
print(comb)