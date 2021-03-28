# Solicitar al usuario 5 números e imprimir su promedio

cantidad, suma = 1, 0
# Bucle while
while cantidad < 6:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    cantidad += 1
# Fin bucle
cantidad -= 1
print("El promedio es:", suma / cantidad)