# TP 06 ej 10
'''Leer una lista de numeros e imprimir el valor minimo y el lugar que ocupa.
Tener en cuenta que el minimo puede estar repetido, en cuyo caso
deberan mostrarse todas las posiciones que ocupe. La carga de datos termina con -1.'''

def minimo(lista):
    # Solo obtengo el menor de la lista
    for j in range(0, len(lista)):
        if j == 0:
            menor = lista[j]
        elif lista[j] < menor:
            menor = lista[j]
    return menor

def indices_menor(lista, menor):
    #
    indices = []
    for j in range(0, len(lista)):
        if menor == lista[j]:
            indices.append(j)
    return indices

lista = []
while True:
    numero = int(input('Ingrese un numero: '))
    if numero != -1:
        lista.append(numero)
    else:
        break
el_menor = minimo(lista)
indices_menores = indices_menor(lista, el_menor)
print(f'El menor es {el_menor}')
print(f'Y está en {indices_menores}')