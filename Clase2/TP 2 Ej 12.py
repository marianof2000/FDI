# TP2 ej 12
# Escribir un programa para convertir un número binario de 4 cifras en un
# número decimal. El número binario se ingresa como un solo número en-
# tero de cuatro dígitos.

# Entrada
binario = int(input("Ingrese el número binario de 4 dígitos: "))
# Variables y proceso
decimal = (binario // 1000) * 8
binario %= 1000
decimal += (binario // 100) * 4
binario %= 100
decimal += (binario // 10) * 2
decimal += binario % 10
# Salida
print(type(decimal))
print("Es el número:", decimal)