def readmoney(msg):
    valid = False
    while not valid:
        entrance = str(input(msg))
        if entrance.isalpha() or entrance.strip() == '':
            print(f'ERRO! \"{entrance}\" is a invalid price.')
        else:
            valid = True
            return float(entrance)