#Creating a currency package:
from ex112.currencyutilitiesCB import dataCB
from ex112.currencyutilitiesCB import currencyCB


currencychose = str(input('Choose a currency: ')).upper().strip()[0:3]
p = dataCB.readmoney('Price: ')
rate = float(input('Rate: '))

currencyCB.summary(p,rate,True)