#Arithmetic progression (while; improved)

prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))

counter = 1
termo = 0
user = -1
tam = 10  # quantidade de loops (termos)

while True:
    while counter < tam:
        termo += raz
        counter += 1
        print(termo)
    user = int(input("Mais termos: \n"))

    if user == 0:
        break
    user += counter
    tam = user

print("Fim.")