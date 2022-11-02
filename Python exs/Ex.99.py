#Biggest number from a list:

from time import sleep

def biggest(* num):
    count = big = 0

    for n in num:
        print(f'{n} ',end='')
        sleep(0.3)
        if count == 0:
            big = n
        else:
            if n > big:
                big = n
        count += 1
    print()
    print('Analyzing data...')
    sleep(0.6)
    print()
    print(f'Total: {count} values.')
    print(f'The biggest number from the list is {big}.')
    print('-'*40)
    sleep(0.6)

biggest(2,9,4,5,7,1)
biggest(4,7,0)
biggest(1,2)
biggest(6)
biggest()
