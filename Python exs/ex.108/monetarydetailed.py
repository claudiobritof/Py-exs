def half(p=0):
    r = p / 2
    return f'{r:.2f}'


def double(p=0):
    r = p * 2
    return f'{r:.2f}'


def decrease(p=0, rate=0):
    r = p - (p * rate/100)
    return f'{r:.2f}'


def increase(p=0, rate=0):
    r = p + (p * rate/100)
    return f'{r:.2f}'


def currency(p=0,currencychose='US$ '):
    return f'{currencychose}{p}'