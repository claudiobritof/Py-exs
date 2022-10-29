#Multiplication table (improved)

counter = 1

while True:
    n = int(input("Qual tabuada?: \n"))
    if n < 0:
        break
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
print("Programa encerrado.")