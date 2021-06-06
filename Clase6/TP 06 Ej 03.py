'''Ejercicio 3: Determinar si una lista es capicúa.'''

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

capicua = True
largo = len(lista1)
recorrer = largo // 2
for x in range(recorrer):
    if lista1[x] != lista1[largo-x-1]:
        capicua = False
        break
if capicua and largo > 0:
    print(f'La lista es capicúa (palíndromo)')
elif largo == 0:
    print(f'La lista está vacía')
else:
    print(f'Sorry, no es capicúa.')
