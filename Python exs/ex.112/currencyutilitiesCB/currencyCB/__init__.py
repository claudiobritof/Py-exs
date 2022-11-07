#Simple way to write "if":
def half(p=0,formato=False):
    """
    -> Calculate the half of a number.
    :param p: price
    :param formato: currency format
    :return: result of the calculation
    """
    r = p / 2
    if formato is False:
        return f'{r:.2f}'
    else:
        return currency(r)

#Other way to write "if" (not):
def double(p=0,formato=False):
    """
    -> Calculate the double of a number.
    :param p: price
    :param formato: currency format
    :return: result of the calculation
    """
    r = p * 2
    if not formato:
        return f'{r:.2f}'
    else:
        return currency(r)

#Simplified way to write "if":
def decrease(p=0, rate=0,formato=False):
    """
    -> Calculate the decrease of a number given by a certain rate.
    :param p: price
    :param rate: interest rate
    :param formato: currency format
    :return: result of the calculation
    """
    r = p - (p * rate/100)
    return f'{r:.2f}' if not formato else currency(r)


def increase(p=0, rate=0,formato=False):
    """
    -> Calculate the increase of a number given by a certain rate.
    :param p: price
    :param rate: interest rate
    :param formato: currency format
    :return: result of the calculation
    """
    r = p + (p * rate/100)
    return f'{r:.2f}' if not formato else currency(r)


def currency(p=0,currencychose='US$ '):
    """
    -> Puts a certain calculus in the currency format
    :param p: price
    :param currencychose: a country currency chosen by the user
    :return: price in the chosen country currency
    """
    return f'{currencychose}{p:.2f}'


def summary(p=0,rate=0,formato=False):
    print(f'The half of {currency(p)} is {half(p, True)}.')
    print(f'The double of {currency(p)} is {double(p, True)}.')
    print(f'Increasing {rate}% on price: {increase(p, rate, True)}.')
    print(f'Decreasing {rate}% on price: {decrease(p, rate, True)}.')