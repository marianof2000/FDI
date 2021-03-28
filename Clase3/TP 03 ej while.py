# Sumar los números del 1 al 10
# (evitar uso de igual en números)

suma, numero = 0, 1 # Asigna 0 a suma y 1 a numero
while numero < 11: # Sale cuando numero == 11
    suma += numero # Equivale a suma = suma + numero
    numero += 1 # Equivale a numero = numero + 1
print("La suma de los números del 1 al 10 es:", suma)