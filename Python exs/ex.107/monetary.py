def increase(p, rate):
    r = p + (p * rate/100)
    return r

def decrease(p, rate):
    r = p - (p * rate/100)
    return r

def double(p):
    r = p * 2
    return r

def half(p):
    r = p / 2
    return r