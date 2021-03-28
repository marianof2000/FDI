# TP3 ej 3
# Leer un número entero N y determinar si es un número natural (positivo y distin-
# to de 0). Si lo es, imprimirlo junto con su doble. En caso contrario, imprimirlo
# junto con su triple.

# Entrada
numero_n = int(input("Ingrese el número N: "))
# Variables y proceso
if numero_n > 0:
    doble = numero_n * 2
    print("El doble de", numero_n, "es", doble)
else:
    triple = numero_n * 3
    print("El triple de", numero_n, "es", triple)