#People listing and comparing

add_age = add_men = add_women = 0

while True:
    age = int(input("Idade: \n"))
    if age >= 18:
        add_age += 1
    sex = str(input("Sexo: [M / F] \n")).strip().upper()
    if sex == "M":
        add_men += 1
    elif sex == "F":
        if age < 20:
            add_women += 1
    choice = str(input("Continuar? [S / N] \n")).strip().upper()
    if choice == "N":
        print(f"Pessoas com mais de 18: {add_age}.")
        print(f"Homens cadastrados: {add_men}")
        print(f"Mulheres com menos de 20 anos: {add_women}")
        break