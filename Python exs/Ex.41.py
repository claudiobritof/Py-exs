#Athletes categories

atual = date.today().year
nasc = int(input("Ano de nascimento do(a) nadador(a): \n"))
idade = atual - nasc
print("O atleta tem {} anos em {}.".format(idade, atual))


if idade <= 9:
    print("Classificação: Mirim.".format(idade))
elif idade <= 14:
    print("Classificação: Infantil.".format(idade))
elif idade <= 19:
    print("Classificação: Júnior.".format(idade))
elif idade <= 25:
    print("Classificação: Sênior.".format(idade))
else:
    print("Classificação: Master.".format(idade))