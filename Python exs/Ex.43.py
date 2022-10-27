#IMC

m = float(input("Digite seu peso (em kg): \n"))
h = float(input("Digite sua altura (em m): \n"))

imc = (m / (h**2))

if imc < 18.5:
    print("Seu IMC é de: {:.1f}. Você está abaixo do peso.".format(imc))
elif imc < 25:
    print("Seu IMC é de: {:.1f}. Você está no peso ideal.".format(imc))
elif imc < 30:
    print("Seu IMC é de: {:.1f}. Você está com sobrepeso.".format(imc))
elif imc < 40:
    print("Seu IMC é de : {:.1f}. Você está com obesidade.".format(imc))
else:
    print("Seu IMC é de {:.1f}. Você está com obesidade mórbida.".format(imc))