#Do you need to vote?

def vote():
    from _datetime import datetime
    age = datetime.now().year - birthyear

    if age < 18:
        return 'denied'
    if age >= 65:
        return 'optional'
    elif 18 <= age < 65:
        return 'mandatory'

birthyear = int(input('Enter your year of birth: '))
vote()
r = vote()

print(f'Your vote is {r} this year.')