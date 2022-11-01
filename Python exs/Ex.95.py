#Soccer players registration (complete team)

data = {}
goals = []
list = []

while True:
    data.clear()
    data['Name'] = str(input('Player name: ')).capitalize()
    matches = int(input(f'How many matches the player {data["Name"]} has played? '))
    if matches > 0:
        goals.clear()
        for c in range(0,matches):
            goals.append(int(input(f'How many goals in match {c+1}? ')))
            data['Goals'] = goals[:]
            data['Total'] = sum(goals)
    else:
        print('The player hasnt played yet.')
    list.append(data.copy())
    while True:
        more = str(input('Do you wish to continue? [Y] or [N]')).upper().strip()[0]
        if more in 'YN':
            break
        print('ERROR! Please type "Y" or "N"')
    if more == 'N':
        break

print('=-='*31)
print(' Shirt |',end='')
for i in data.keys():
    print(f' {i:<26}|',end='')
print('')
#print(' Shirt  | Name                     | Goals on each match       | Total goals              |')
print('-'*93)

for k,v in enumerate(list):
    print(f'{k:>4}   |',end='')
    for d in v.values():
        print(f' {str(d):<26}|',end='')
    print('')
print('=-='*31)

while True:
    find = int(input('Which player do you want to show data? [999 to stop]'))
    if find == 999:
        break
    if find >= len(list):
        print(f'ERROR! There is no player with shirt number {find}. Try again.')
    else:
        print(f' -- Data for {list[find]["Name"]}:')
        for i,g in enumerate(list[find]['Goals']):
            print(f'The player {list[find]["Name"]} scored {g} goals on match {i+1}.')
    print('-'*40)
print('--FINISHED--')