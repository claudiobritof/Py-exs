#Setting currency (v1)
from monetary import double, half, increase, decrease

p = float(input('Price: US$ '))
print(f'The half of US$ {p} is US$ {half(p)}.')
print(f'The double of US$ {p} is US$ {double(p)}.')
print(f'Increasing 10% on price: US$ {increase(p,10)}.')
print(f'Decreasing 10% on price: US$ {decrease(p,10)}.')