# TP 04 ejercicio 4
'''Realizar un programa para ingresar desde el teclado un conjunto de números e
informar el último elemento ingresado en una posición par. Finalizar la lectura de
datos con el valor -1.'''

numero = 0
ultimo = 0
posicion = 1
while numero != -1:
    numero = int(input(f'Ingrese un número (-1 para salir) '))
    if numero != -1 and posicion % 2 == 0:
        ultimo = numero
    posicion += 1
print(f'El último elemento ingresado en una posición par es el {ultimo}')