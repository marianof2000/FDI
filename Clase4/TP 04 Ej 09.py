# TP 04 ejercicio 9
'''Leer cien números e imprimir su promedio.'''

limite = 100
# Con el FOR
suma = 0
for numero in range(0, limite + 1):
    numero = int(input(f'Ingrese un número: '))
    suma += numero
print(f'El promedio de los 100 números es: {round((suma/limite), 2)}')

# Con el WHILE
suma = 0
contador = 0
while contador < limite + 1:
    numero = int(input(f'Ingrese un número: '))
    suma += numero
    contador += 1
print(f'El promedio de los 100 números es: {round((suma/limite), 2)}')