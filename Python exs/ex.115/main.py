from ex115arquivo import *
from time import sleep
from ex115arquivo.archive import *

archive = 'archive.txt'

if not archiveexist(archive):
    createarchive(archive)

menu()

while True:
    option = int(input('Your option: '))
    if option == 1:
        #ver pessoas cadastradas
        readfile(archive)

    elif option == 2:
        #cadastrar novas pessoas
        name = str(input('Name: ')).capitalize()
        age = int(input('Age: '))
        register(archive,name,age)

    elif option == 3:
        #Exit
        print('Exited. Thanks!')
        break
    else:
        print('ERROR! Please type again.')


#nome
#idade

#cadastrar nova pessoa?
#listar pessoas cadastradas