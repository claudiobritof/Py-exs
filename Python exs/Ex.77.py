#Words tuple


tupla = (
    "Beatles", "Elvis", "BB King",
    "Kendrick Lamar", "Charlotte", "Rocket", "Amanda"
    )

vogais = ["a", "e", "i", "o", "u"]

for nome in tupla:
    nome = str(nome).lower()
    lista = []

    for letra in nome:
        for i in vogais:
            if letra == i:
                lista.append(letra)

    print(f"{nome.capitalize()}: {lista} - {len(lista)} vogais")
    del(lista)