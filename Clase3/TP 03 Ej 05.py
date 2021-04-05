'''
Desarrollar un programa para leer la base y la altura de un triángulo e imprimir
su superficie. El algoritmo debe validar los datos de entrada, verificando que
éstos sean números positivos. En caso contrario debe imprimirse el dato erróneo
junto con una leyenda aclaratoria. Se recuerda que Sup = (Base * Altura) / 2.
'''

base = float(input('Ingrese la base del triángulo '))
while base <=0:
    print(f'{base} no es un número positivo')
    base = float(input('Ingrese la base del triángulo '))
altura = float(input('Ingrese la altura del triángulo '))
while altura <=0:
    print(f'{altura} no es un número positivo')
    altura = float(input('Ingrese la altura del triángulo '))
superficie = base * altura / 2
print()
print(f'La superficie del triángulo es {superficie}')