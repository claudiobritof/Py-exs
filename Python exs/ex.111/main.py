#Creating a currency package:
from ex111 import currencyutilitiesCB

currencychose = str(input('Choose a currency: ')).upper().strip()[0:3]
p = float(input(f'Price: {currencychose} '))
rate = float(input('Rate: '))

print(summary(p))