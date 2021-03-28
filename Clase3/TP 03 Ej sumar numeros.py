# Solicitar al usuario la cantidad de números que el usuario
# quiere sumar, luego pedir uno a uno dichos números y
# por último imprimir la suma de los mismos 

indice, suma = 0, 0
cantidad = int(input("Ingrese la cantidad de números a sumar: "))
# Comienzo bucle
while indice < cantidad:
    numero = int(input("Ingrese el numero: "))
    suma += numero
    indice += 1
# Fin del bucle
print()
print("La suma de todos los números es:", suma)