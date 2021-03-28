# Solicitar al usuario 5 números e imprimir el mayor

mayor, cantidad = 0, 1
numero = int(input("Ingrese un número: "))
mayor = numero
# Inicio de bucle
while cantidad < 5:
    numero = int(input("Ingrese un número: "))
    cantidad += 1
    if numero > mayor:
        mayor = numero
# Fin del bucle
print()
print("El mayor de los números es:", mayor)