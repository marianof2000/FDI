'''Ejercicio 7: Escribir una función para devolver la posición que ocupa un valor pasado como
parámetro, utilizando búsqueda secuencial en una lista desordenada. La función
debe devolver -1 si el elemento no se encuentra en la lista.'''

def buscar_elemento(valor):
    largo_lista = len(lista_a)
    posicion = -1
    for j in range(0, largo_lista):
        if lista_a[j] == valor:
            return j
    return posicion

lista_a = [50, 15, 56, 14, 35, 1, 12, 9]
dato = int(input('Que valor desea buscar? '))
lugar = buscar_elemento(dato)
if lugar != -1:
    print(f'El valor {dato} está en la posición {lugar + 1}')
else:
    print(f'No se encontró el valor {dato}')