#Countdown (using def):

from time import sleep

def cont(a,b,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Countdown from {a} to {b} with a {p} pace:')
    sleep(0.1)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ',end='')
            cont += p
            sleep(0.3)
        print()
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.3)
        print()
cont(1,10,1)
cont(10,0,2)
cont(a=int(input('Start: ')),b=int(input('End: ')),p=int(input('Pace: ')))