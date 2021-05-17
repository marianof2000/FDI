# TP 04 ejercicio 10
'''Desarrollar un programa que imprima los números impares comprendidos entre
1 y 1000.'''

# Con el FOR
for numero in range(1, 1001, 2):
    print(f'Los impares son: {numero}')
    
print()

# Con el WHILE
numero = 1
while numero < 1001:
    if numero % 2 != 0:
        print(f'Los impares son: {numero}')
    numero += 1