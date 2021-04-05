''' TP 03 Ej 07
Una empresa aplica el siguiente procedimiento en la comercialización de sus pro-
ductos:
Aplica el precio base a la primera docena de unidades.
Aplica un 10% de descuento a todas las unidades entre 13 y 100.
Aplica un 25% de descuento a todas las unidades por encima de las 100.
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
base es 100. El cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
Desarrollar un programa que lea la cantidad solicitada de un producto y su pre-
cio base, e imprima el valor total de la venta y el precio promedio.
'''
precio_venta = 0
precio_prom = 0
cantidad = 0
precio = int(input('Ingrese el precio de la unidad '))
while precio <= 0:
    print(f'El precio debe ser mayor que cero')
    precio = int(input('Ingrese el precio de la unidad '))
cantidad = int(input('Ingrese la cantidad de unidades '))
while cantidad <= 0:
    print(f'La cantidad debe ser mayor que cero')
    cantidad = int(input('Ingrese la cantidad de unidades '))
if cantidad > 100:
    precio_venta += precio * (12 + 0.75 * (cantidad - 100) + 0.9 * 88)
elif cantidad > 12:
    precio_venta += precio * (12 + 0.9 * (cantidad - 12))
else:
    precio_venta = precio * cantidad
precio_prom = precio_venta / cantidad
print(f'El precio de venta para {cantidad} unidades será de $ {round(precio_venta, 2)}')
print(f'y el precio promedio es de $ {round(precio_prom, 2)}')
