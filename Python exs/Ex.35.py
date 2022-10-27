#Triangles validation

print('-='*20)
print('Triangles validation')
print('-='*20)

r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('The segments can form a triangle.')
else:
    print('The segments cannot form a triangle.')