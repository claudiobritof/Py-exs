#Setting currency (v3)
from ex109 import monetarydetailed
from monetarydetailed import half,double,increase,decrease

currencychose = str(input('Choose a currency: ')).upper().strip()[0:3]
p = float(input(f'Price: {currencychose} '))
rate = float(input('Rate: '))

print(f'The half of {monetarydetailed.currency(p)} is {monetarydetailed.half(p,True)}.')
print(f'The double of {monetarydetailed.currency(p)} is {monetarydetailed.double(p,True)}.')
print(f'Increasing {rate}% on price: {monetarydetailed.increase(p,rate,True)}.')
print(f'Decreasing {rate}% on price: {monetarydetailed.decrease(p,rate,True)}.')