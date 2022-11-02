#Validating an integer input without using "int":

def readint(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('\033[0;31mERROR! Type a valid integer number.\033[m')
        if ok:
            break
    return value

n = readint('Type a number: ')
print(f'You typed the number {n}.')

#funcao leiaint() que vai funcionar como um input() mas que vai fazer a validação pra aceitar apenas valor int
