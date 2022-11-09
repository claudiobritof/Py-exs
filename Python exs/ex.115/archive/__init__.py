def menu():
    print('-' * 40)
    print('MENU'.center(40))
    print('-' * 40)
    print('1 - See registration list')
    print('2 - Register new person')
    print('3 - Exit')
    print('-' * 40)


def archiveexist(name):
    try:
        a = open(name, 'rt') #read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createarchive(name):
    try:
        a = open(name, 'wt+')  #write text create(+)
        a.close()
    except:
        print('Error while creating the file.')
    else:
        print(f'File {name} created with success.')


def readfile(name):
    try:
        a = open(name, 'rt')
    except:
        print('There was an error while reading the file.')
    else:
        menu()
        for line in a:
            data = line.split(';')
            data[1] = data[1].replace('\n','')
            print(f'{data[0].ljust(30)}{data[1]} years.')
    finally:
        a.close()


def register(archive, name='unknown',age=0):
    try:
        a = open(archive, 'at+')   #at+ = append text file
    except:
        print('There was an error while opening the file.')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('There was an error while writing data.')
        else:
            print(f'New register of {name} added.')
            a.close()