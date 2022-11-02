#Intro to defs:

def write(txt):
    size = len(txt) + 4
    print('-'*size)
    print(txt.capitalize().strip().center(size))
    print('-'*size)


write('1')
write('2')
write('3')