#Sum of random numbers:

from random import randint
from time import sleep

def sort(parameter):
    print('Generating 5 numbers:')
    for c in range(0,5):
        parameter.append(randint(1,20))


parameter = []
sort(parameter)
print(parameter)


def sumpairs(parameter):
    soma = 0
    for v in parameter:
         if v % 2 == 0:
            soma += v
    print(f'The sum of pair values in {parameter} is equal to {soma}.')


sumpairs(parameter)