# TP4 Ejercicio 13 (pensado con funciones)

def es_menor(num1, num2):
    # Posición del menor número
    if num1 < num2:
        return True
    pass

posicion = 1
menor = int(input('Ingrese el primer número '))

for contador in range(2, 11):
    numero = int(input('Ingrese los restantes números: '))
    if es_menor(numero, menor):
        menor = numero
        posicion = contador
print()
print (f'El numero menor es: {menor} ')
print (f'La posición en que se encuentra el numero menor es la: {posicion}')