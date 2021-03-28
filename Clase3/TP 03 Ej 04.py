# TP3 ej 4
"""
Ingresar dos números enteros A y B. Desarrollar un programa que determine si
A es múltiplo de B y si B es múltiplo de A. Imprimir mensajes aclaratorios.
"""

# Entrada
numero_a = int(input("Ingrese el número A: "))
numero_b = int(input("Ingrese el número B: "))
# Variables y proceso
if (numero_a != 0) and (numero_b != 0):
    if (numero_a % numero_b == 0) or (numero_b % numero_a == 0):
        if (numero_a % numero_b) == 0:
            print("El número A es múltiplo de B")
        if (numero_b % numero_a) == 0:
            print("El número B es múltiplo de A")
    else:
        print("Ninguno es múltiplo de ninguno")
else:
    print("Uno de los dos o ambos son cero")

"""
# Variante de código
if (numero_a != 0) and (numero_b != 0):
    if (numero_a % numero_b) == 0:
        print("El número A es múltiplo de B")
    elif (numero_b % numero_a) == 0:
        print("El número B es múltiplo de A")
    else:
        print("Ninguno es múltiplo de ninguno")
else:
    print("Uno de los dos o ambos son cero")
"""