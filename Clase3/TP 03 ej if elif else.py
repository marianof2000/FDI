# Ejemplo de if else

importe = int(input("Ingrese el importe a pagar: "))
# Estructura if else
if importe > 10000:
    print("El descuento va a ser del 10%")
    descuento = importe * 0.1 # Equivale a un 10% de descuento
elif importe > 3000:
    print("El descuento va a ser del 5%")
    descuento = importe * 0.05 # Equivale a un 5% de descuento
else:
    print("No hay descuento!!")
    descuento = 0 # Equivale a un 0% de descuento
# Salida por pantalla
print("El importe a pagar es:", importe-descuento)