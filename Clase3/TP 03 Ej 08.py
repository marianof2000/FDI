''' TP 03 ej 08
Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga
su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento
de $120 o del 2% de la factura, lo que resulte menor. Si paga en los siguientes
10 días del mes deberá pagar el importe original de la factura, mientras que si
paga después del día 20 deberá abonar una multa de $150 o del 10% de su fac-
tura, lo que resulte mayor. Desarrolle un programa que lea el número del cliente
y el total de la factura, y emita un informe donde conste el número del cliente y
los tres importes que podrá abonar según la fecha de pago.
'''
imp_factura = 0
importe_1 = 0
importe_2 = 0
importe_3 = 0
cliente = input('Ingrese el número de cliente ')
imp_factura = float(input('Ingrese el monto de la factura a cancelar '))
while imp_factura <= 0:
    print(f'El importe debe ser mayor que cero')
    imp_factura = float(input('Ingrese el monto de la factura a cancelar '))
# Importe a los 10 días
if 120 <= imp_factura * 0.02:
    importe_1 = imp_factura - 120
else:
    importe_1 = imp_factura / 1.02
# Importe luego de 10 días
importe_2 = imp_factura
# Importe luego de 20 días
if 150 > imp_factura * 0.1:
    importe_3 = imp_factura + 150
else:
    importe_3 = imp_factura * 1.1
print(f'El cliente nro {cliente} deberá pagar:')
print(f'antes de 10 días $ {round(importe_1, 2)}')
print(f'luego de 10 días $ {round(importe_2, 2)}')
print(f'después de 20 días $ {round(importe_3, 2)}')