def readint(msg):
    ok = False
    value = 0
    while True:
        try:
            i = int(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERROR! Type a valid integer number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUser preferred not to type this number.\033[m')
            return 0
        else:
            return i


def readfloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERROR! Type a valid float number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mUser preferred not to type this number.\033[m')
            return 0
        else:
            return f