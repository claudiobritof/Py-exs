#Area

largura = float(input("Digite a largura: \n"))
altura = float(input("Digite a altura: \n"))
area = largura * altura

print("A parede tem a dimensão {}x{} e sua área é de {}m².".format(largura, altura, area))

tinta_necessaria = area / 2
print("Para pintá-la, precisará de {}L de tinta.".format(tinta_necessaria))