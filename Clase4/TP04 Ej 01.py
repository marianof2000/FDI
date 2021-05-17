# TP 04 ejercicio 1
'''Realizar un programa para ingresar desde el teclado un conjunto de números.
Mostrarlos a medida que se los ingresa. Finalizar la lectura de datos con el valor
-1.'''

numero = 0
while numero != -1:
    numero = int(input(f'Ingrese un número (-1 para salir) '))
    if numero != -1:
        print(numero)
