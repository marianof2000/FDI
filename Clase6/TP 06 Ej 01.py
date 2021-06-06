'''Ejercicio 1:
Escribir una función para ingresar desde el teclado una serie de números entre 1
y 20 y guardarlos en una lista. En caso de ingresar un valor fuera de rango el
programa mostrará un mensaje de error y solicitará un nuevo número. Para fi-
nalizar la carga se deberá ingresar -1. La función no recibe ningún parámetro, y
devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de
retorno.'''

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