# TP 04 ejercicio 12
'''Leer dos números A y B enteros positivos. Calcular el producto A * B por sumas
sucesivas e imprimir el resultado. Ejemplo: 4 * 3 = 4 + 4 + 4 (4 sumado 3 ve-
ces).'''

producto = 0
numero_a = int(input(f'Ingrese el número A: '))
numero_b = int(input(f'Ingrese el número B: '))
for indice in range(0, numero_b):
    producto += numero_a
print(f'El producto es: {producto}')
