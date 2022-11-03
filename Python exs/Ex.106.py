#Interactive help system (coloured):

from time import sleep


c = ('\033[m',         # 0 - no color
     '\033[0;30;41m',  # 1 - red
     '\033[0;30;42m',  # 2 - green
     '\033[0;30;43m',  # 3 - yellow
     '\033[0;30;44m',  # 4 - blue
     '\033[0;30;45m',  # 5 - purple
     '\033[7;30m',     # 6 - white
     );


def helpdef(com):
    title(f'Accessing comand manual \'{com}\'',4)
    print(c[6],end='')
    help(com)
    print(c[2],end='')
    sleep(0.2)

def title(msg, color=0):
    size = len(msg) + 4
    print(c[color],end='')
    print('~' * size)
    print(msg)
    print('~' * size)
    print(c[4], end='')
    sleep(0.2)

comand = ''
while True:
    title('HELP SYSTEM PYTHON', 2)
    comand = str(input('Function or Library > '))
    if comand.upper() == 'END':
        break
    else:
        help(comand)
title('See ya!', 1)