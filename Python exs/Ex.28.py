#Random number game

from random import randint
from time import sleep
ran = randint(0, 5)

print("--=--" * 15)
print("Calculando um número entre 0 e 5.")
print("--=--" * 15)
num = int(input("Qual número foi calculado?: \n"))
print("Calculando...")
sleep(1)

if num > 5 or num < 0:
    if num < 0:
        print("O número não pode ser negativo.")
    else:
        print("Dica: o número está entre 0 e 5!")
else:
    if num == ran:
        print("Número digitado: {}.".format(num))
        print("Parabéns, você venceu!")
    else:
        print("Número digitado: {}.".format(num))
        print("VOCÊ ERROU. \nO número correto era {}. Tente novamente.".format(ran))