#Unique tuple


listagem = (
    "pão", 1,
    "leite", 3.50,
    "frango", 10.90
      )

print("=" * 35)
print("Tela preta, letra verde.")
print("=" * 35)

produto = 0
preco = 1

for item in range(0, len(listagem)// 2):
    print(f"{listagem[produto]:.<30} R${listagem[preco]:>7.2f}")
    preco += 2
    produto += 2