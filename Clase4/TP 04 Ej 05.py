# TP 04 ejercicio 5
'''Realizar un programa para ingresar desde el teclado un conjunto de números e
informar los elementos ingresados menores a un valor ingresado previamente.
Finalizar la lectura de datos con el valor -1.'''

menor = int(input(f'Ingrese el número para comparar los menores a él: '))
numero = 0
while numero != -1:
    numero = int(input(f'Ingrese un número (-1 para salir): '))
    if numero != -1 and numero < menor:
        print(f'El {numero} es menor a {menor}')
# print(f'El último elemento ingresado en una posición par es el {ultimo}')