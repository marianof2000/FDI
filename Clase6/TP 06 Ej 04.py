# TP 06 ej 04
# 4. Invertir un arreglo de 20 números enteros.
# Sin modificar el original

def invertir_lista(lista1):
    # Función para invertir una lista
    # (no puedo usar el mismo nombre de lista que en el bloque principal)
    # tengo que hacer una copia de lista -> lista_tmp
    # lista_tmp = list(lista1)
    lista_tmp = lista1.copy()
    largo = len(lista_tmp)
    # Si la longitud es impar no invierto el del medio
    mitad = largo // 2
    for j in range(0, mitad):
        # Esta rutina intercambia los valores el primero con el último
        # y así con todos
        temporal = lista_tmp[j]
        lista_tmp[j] = lista_tmp[largo-j-1]
        lista_tmp[largo-j-1] = temporal
    # Retorna la lista invertida
    return lista_tmp
    pass

# Carga automáticamente la lista con números desde el 1 hasta el 10
lista = list(range(1, 12))
print(lista)
lista_invertida = invertir_lista(lista)
print(lista)
print(lista_invertida)