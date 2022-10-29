#ATM

from datetime import datetime
from time import sleep

num = int(input('''Bank
Digite o valor que você deseja sacar: \nR$ '''))

if num <= 50:
    print("Aguarde a contagem das notas...")
    sleep(0.25)
elif num <= 100:
    print("Aguarde a contagem das notas...")
    sleep(0.5)
else:
    print("Aguarde a contagem das notas...")
    sleep(0.75)

print("Sacando:\n")

cedulas = [50, 20, 10, 1]

while num > 0:  # Enquanto a variável num não estiver vazia,
    for i in cedulas:
        cedulas = num // i  # Cedulas recebe a quantidade de cédulas disponíveis
        num %= i  # Num recebe o resto (%) de num / i
        # print(cedulas)
        if cedulas > 0:  # Se houver cédulas disponíveis,
            print(f"{cedulas} notas de R${i}")

now = datetime.now().hour

if now <= 12:
    now = "bom dia"
elif now <= 19:
    now = "boa tarde"
elif now <= 23:
    now = "boa noite"

print(f"\nAgradecemos a preferência. \nTenha um(a) {now}.")