# TP3 ej 1
# Ingresar dos números A y B e imprimir el mayor, o cualquiera si son iguales.

# Entrada
numero_a = int(input("Ingrese el número A: "))
numero_b = int(input("Ingrese el número B: "))
# Variables y proceso
if numero_a != numero_b:
    if numero_a > numero_b:
        print("El número mayor es:", numero_a)
    else:
        print("El número mayor es:", numero_b)
else:
    print("Ambos son iguales:", numero_a)