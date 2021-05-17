'''Realizar un programa para ingresar desde el teclado un conjunto de números e
informar si la cantidad de elementos es impar o par, sin utilizar contadores.
Finalizar la lectura de datos con el valor -1.'''

impar = False # Cambia si es par o impar

numero = 0
while numero != -1:
    numero = int(input('Ingrese un número (-1 para salir): '))
    # Cambio de par a impar si es distinto de -1
    if numero != -1:
        # Hago cambiar el estado de cantidad para a impar
        if impar: 
            impar = False
        else:
            impar = True
            
if impar:
    print(f'La cantidad de números ingresada es impar')
else:
    print(f'La cantidad de números ingresada es par')