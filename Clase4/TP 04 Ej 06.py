# TP 04 ejercicio 6
'''Realizar un programa para ingresar desde el teclado un conjunto de números e
informar en forma separada la cantidad de elementos pares e impares ingresa-
dos. Finalizar la lectura de datos con el valor -1.'''

pares = 0
impares = 0
numero = 0
while numero != -1:
    numero = int(input(f'Ingrese un número (-1 para salir): '))
    if numero != -1:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Se ingresaron {pares} números pares')
print(f'Y se ingresaron {impares} números impares')