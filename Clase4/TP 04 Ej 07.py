# TP 04 ejercicio 7
'''Realizar un programa para ingresar desde el teclado un conjunto de números y
mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
con un valor -1.'''

mayor = 0
menor = 0
numero = 0
vez = 1
while numero != -1:
    numero = int(input(f'Ingrese un número (-1 para salir): '))
    if numero != -1:
        if vez == 1:
            mayor = numero
            menor = numero
            vez = 0
        if numero > mayor:
            mayor = numero
        elif numero < menor:
            menor = numero
if vez == 0:
    print(f'El número mayor es {mayor}')
    print(f'Y el menor es {menor}')
else:
    print(f'No se ingresaron números a comparar.')