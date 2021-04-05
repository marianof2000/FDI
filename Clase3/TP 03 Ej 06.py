''' TP 03 Ej 06
Una editorial determina el precio de un libro según la cantidad de páginas que
contiene. El costo básico del libro es de $125, más $2,20 por página con encua-
dernación rústica. Si el número de páginas supera las 300 la encuadernación
debe ser en tela, lo que incrementa el costo en $80. Además, si el número de
páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-
cuadernación que incrementa el costo en $136. Desarrollar un programa que
calcule el costo de un libro dado el número de páginas.
'''
paginas = int(input('Ingrese el número de páginas del libro '))
while paginas <= 0:
    print(f'La cantidad de páginas debe ser mayor a 0')
    paginas = int(input('Ingrese el número de páginas del libro '))
costo = 125 + 2.2 * paginas
if paginas >= 300:
    costo += 80
    if paginas >= 600:
        costo += 136
# Otra forma de escribir el costo en una sola línea usando lógica booleana        
# costo = 125 + 2.2 * paginas + (paginas >= 300) * 80 + (paginas >= 600) * 136 
print(f'El costo del libro de {paginas} paǵinas será de $ {round(costo, 2)}')