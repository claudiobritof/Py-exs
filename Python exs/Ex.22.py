#Complete name

nome = str(input("Digite seu nome: \n")).strip()

# O nome com todas as letras maiúsculas
print("Nome em maiúsculas: {}.".format(nome.upper()))

# O nome com todas minúsculas
print("Nome em minúsculas: {}.".format(nome.lower()))

# Quantas letras ao todo (sem considerar espaços)
print("Letras ao todo: {}.".format(len(nome) - nome.count(" ")))

# Quantas letras tem o primeiro nome:
nome = nome.split()
print('O primeiro nome é "{}" e ele tem {} letras.'.format(nome[0], len(nome[0])))