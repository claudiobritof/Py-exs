#People registration

list = []
person = {}
totalage = averageage = 0
women = []
highage = []

while True:
    person.clear()
    person['name'] = str(input('Name: ')).capitalize()
    while True:
        person['genre'] = str(input('Genre: [M] or [F]')).upper().strip()[0]
        if person['genre'] in 'MF':
            break
        print('ERROR! Please type "M" or "F"')
    person['age'] = int(input('Age: '))
    list.append(person.copy())
    totalage += person['age']
    while True:
        more = str(input('Do you wish to continue? [Y] or [N]')).upper().strip()[0]
        if more in 'YN':
            break
        print('ERROR! Please type "Y" or "N"')
    if more in 'N':
        break
print('=-='*30)

#a) how many people registered?

print(f'a) A total of {len(list)} people was registered.')

#b) average of age

averageage = totalage/(len(list))
print(f'b) The average of age is equal to {averageage:5.2f} years.')

#c) only women list

for p in list:
    if p['genre'] == 'F':
        women.append(p)
print(f'c) Only women list: {women}')

#d) list of people with age higher than average

for p in list:
    if p['age'] > averageage:
        highage.append(p)
print(f'd) List of people with higher age than average: {highage}')