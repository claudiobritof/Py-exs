#Setting currency (v2)
from ex108 import monetarydetailed

currencychose = str(input('Choose a currency: '))
p = float(input(f'Price: {currencychose} '))
rate = float(input('Rate: '))

print(f'The half of {currencychose} {p:.2f} is {currencychose} {monetarydetailed.half(p)}.')
print(f'The double of {currencychose} {p:.2f} is {currencychose} {monetarydetailed.double(p)}.')
print(f'Increasing {rate}% on price: {currencychose} {monetarydetailed.increase(p,rate)}.')
print(f'Decreasing {rate}% on price: {currencychose} {monetarydetailed.decrease(p,rate)}.')