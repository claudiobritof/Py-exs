#Arithmetic progression

prim = int(input("Primeiro termo: \n"))
raz = int(input("Digite a razão da PA: \n"))
dec = prim + (10 - 1) * raz  # Fórmula do enésimo termo de uma PA.
for c in range(prim, dec, raz):
    print("{}".format(c), end=",")
print("\nFim.")