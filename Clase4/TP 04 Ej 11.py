# TP 04 ejercicio 11
'''Leer diez números enteros e imprimir el mayor.'''

# Con el FOR
for indice in range(0, 10):
    numero = int(input(f'Ingerse un número: '))
    if indice == 0: # Verifico si es el primero ingresado
        mayor = numero
    elif numero > mayor:
        mayor = numero
print(f'El número mayor es: {mayor}')
