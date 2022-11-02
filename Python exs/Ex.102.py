#Factorial (using def and docstrings)

def factorial(n, show=False):

    f = 1
    for c in range(n,0,-1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ',end='')
        f *= c
    return f

print(factorial(30, show=True))
help(factorial)