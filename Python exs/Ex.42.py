#Triangles validation (remake)

a = float(input("Primeiro segmento de reta: \n"))
b = float(input("Segundo segmento de reta: \n"))
c = float(input("Terceiro segmento de reta: \n"))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("O triângulo que existe é um ", end="")
    if a == b == c:
        print("triângulo EQUILÁTERO.")
    elif (a == b) or (a == c) or (b == c):
        print("triângulo ISÓSCELES.")
    else:
        print("triângulo ESCALENO.")
else:
    print("O triângulo inexiste.")