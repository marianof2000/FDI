# TP4 Ejercicio 13 (pensado con funciones)

def es_menor(num1, num2):
    # Posición del menor número
    if num1 < num2:
        return True
    pass

contador = 1
numero = int(input('Ingrese 10 numeros: '))
menor = numero
posicion = contador
while contador < 10 :
    numero = int(input('Ingrese 10 numeros: '))
    contador +=1
    if es_menor(numero, menor):
        menor = numero
        posicion = contador
print()
print (f'El numero menor es: {menor} ')
print (f'La posición en que se encuentra el numero menor es: {posicion}')