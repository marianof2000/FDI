lista = ['a', 'b', 'c', 'd', 'e']
print(lista)
# Primera forma tengo que usar j que va desde 0 hasta 5
for j in range(0, len(lista)):
    # Acá imprimo la lista con el índice
    print(lista[j]) # Acá uso la lista y el índice
print()
# Segunda forma uso a j que va desde 'a' hasta 'e'
for j in lista:
    # Acá imprimo los elementos de la lista
    # Acá uso solo la variable que tiene el dato de la lista
    # pero no tiene el índice
    print(j) 
