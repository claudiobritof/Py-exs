#Setting currency (v_final)
from ex110 import monetarydetailed

currencychose = str(input('Choose a currency: ')).upper().strip()[0:3]
p = float(input(f'Price: {currencychose} '))
rate = float(input('Rate: '))

print(summary(p))