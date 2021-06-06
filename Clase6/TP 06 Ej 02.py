'''Ejercicio 2: Calcular la suma de los números de una lista.'''

def carga_lista():
    # Carga numeros en una lista
    lista = []
    numero = 0
    while numero != -1:
        numero = int(input('Ingrese un número (-1 para salir): '))
        if numero >= 0 and numero <= 20:
            # NombreLista.append(dato) agrega un elemento a la lista en una nueva posición
            lista.append(numero)
        elif numero != -1:
            print(f'El número está fuera de rango')
    return lista

lista1 = carga_lista()
print(lista1)

# Forma 1 indexada
suma = 0
for x in range(len(lista1)):
    # Los nombramos por su índice
    suma += lista1[x]
print(f'La suma de todos los elementos de la lista es {suma}')

# Forma 2 por elemento
suma = 0
for x in lista1:
    # Los listamos por elemento de la lista
    suma += x
print(f'La suma de todos los elementos de la lista es {suma}')