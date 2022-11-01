#Practicing dictionaries

studentname = {}

studentname['name'] = str(input('Digit student name: '))
studentname['average'] = float(input(f'{studentname["name"]} average: '))

if studentname['average'] >= 7.0:
    studentname['situation'] = 'Approved'
elif 5 <= studentname['average'] < 7:
    studentname['situation'] = 'Finals test'
else:
    studentname['situation'] = 'Reproved'

for k,v in studentname.items():
    print(f'{k} is equal to {v}.')