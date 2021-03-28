# TP3 ej 2
# Leer un número entero A e imprimir un mensaje indicando si es par o impar.
# https://es.wikipedia.org/wiki/Paridad_del_cero

# Entrada
numero_a = int(input("Ingrese el número A: "))
# Variables y proceso
if (numero_a % 2) != 0:
    print("El número", numero_a, "es impar")
else:
    print("El número", numero_a, "es par")