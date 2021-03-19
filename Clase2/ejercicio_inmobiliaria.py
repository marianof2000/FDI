# Ejercicio Inmobiliaria

# El salario fijo mensual de base
salario = 8000
# Se debe detallar la cantidad de ventas que se hicieron porque se pagará $500 por cada una
cantidad_de_ventas = int(input("Ingrese cantidad de ventas: "))
# Se debe ingresar el total de lo que vendió para calcular el porcentaje a pagarle al vendedor, es el 2%
total_de_ventas = int(input("Ingrese el importe total de ventas: "))
# comision= 500 * cVentas
# porcentaje = 0.02 * iTotal
a_pagar = salario + 500 * cantidad_de_ventas + total_de_ventas * 0.02
print("Total a pagar:", a_pagar)
