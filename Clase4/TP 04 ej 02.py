primer = 0
es_quinto = 1
ultimo = 0
numero = 0
cantidad = 1

while numero != -1:
    numero = int(input('Ingrese el número: '))
    if es_primero == 1:
        es_primero = 0
        primer = numero 
    if numero != -1:
        ultimo = numero

print(f'El primero es {primer} y el último es {ultimo}')