# Método de burbuja sin optimizar
# Ordenar lista de menor a mayor
# lista_a = [1, 9, 15, 14, 12, 35, 56, 50]
lista_a = [50, 15, 56, 14, 35, 1, 12, 9]
print(f'Lista sin ordenar {lista_a}')
largo_lista = len(lista_a)
# Para que sea completo el ordenmiento tiene que recorrer al menos
# largo_lista veces -1 para que quede ordenado
# "Anidammos" los for (bucles)
for i in range(0, largo_lista - 1):
    # Recorre una vez la lista haciendo ordenamiento
    hubo_cambios = False
    for j in range(0, largo_lista - 1):
        if lista_a[j] > lista_a[j + 1]:
            aux = lista_a[j]
            lista_a[j] = lista_a[j + 1]
            lista_a[j + 1] = aux
            hubo_cambios = True
    # Veo como la va ordenando
    print(lista_a)
    # Evita hacer recorridos si ya está ordenado o si no hubo cambios
    if not(hubo_cambios):
        print(f'Cortó antes, en {i} vueltas')
        break
print(f'Lista ordenada {lista_a}')
