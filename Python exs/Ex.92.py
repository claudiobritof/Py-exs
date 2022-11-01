#Worker Registration

from _datetime import datetime

registration = {}

registration['name'] = str(input('Name: '))
year = int(input('Year of birth: '))
age = datetime.now().year - year
registration['age'] = age
registration['CTPS'] = int(input('CTPS: [0 if none]'))

if registration['CTPS'] != 0:
    registration['hireyear'] = int(input('Year of hiring: '))
    registration['salary'] = float(input('Salary: '))
    registration['retirement'] = registration['age'] + ((registration['hireyear'] + 35) - datetime.now().year)

print('=-='*20)

for k,v in registration.items():
    print(f'{k.capitalize()} is equal to {v}.')