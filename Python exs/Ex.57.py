#Gender

sex = str(input("Digite M ou F: \n")).strip().upper()[0]
while sex not in "MmFf":
    sex = str(input("Erro. Digite só M ou F: \n")).strip().upper()[0]
print("Sexo {} registrado com sucesso.".format(sex))