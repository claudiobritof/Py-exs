#43'

#Area calculation of a rectangle
def area(b,h):
    a = b * h
    print(f'The full area of the terrain with sides {b} x {h} is equal to {a:.2f}m².')


#Função principal:
b = float(input('Lenght of the base: '))
h = float(input('Lenght of the height: '))
area(b,h)