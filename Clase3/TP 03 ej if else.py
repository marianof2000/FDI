# Ejemplo de if else

importe = int(input("Ingrese el importe a pagar: "))
# Estructura if else
if importe < 1000:
    print("El descuento va a ser del 5%")
    descuento = importe * 0.05 # Equivale a un 5% de descuento
else:
    print("El descuento va a ser del 10%")
    descuento = importe * 0.1 # Equivale a un 10% de descuento
# Salida por pantalla
print("El importe a pagar es:", importe-descuento)