# TP2 ej 9
# Una inmobiliaria paga a sus vendedores un salario de $800, más una
# comisión de $50 por cada venta realizada, más el 5% del valor de esas
# ventas. Realizar un programa que imprima el número del vendedor y el
# salario que le corresponde en un determinado mes. Se leen el número
# del vendedor, la cantidad de ventas que realizó y el valor total de las
# mismas.

# El salario fijo mensual de base
salario = 800
vendedor = int(input("Ingrese el número de vendedor: "))
# Se debe detallar la cantidad de ventas que se hicieron porque se pagará $500 por cada una
cantidad_de_ventas = int(input("Ingrese cantidad de ventas: "))
# Se debe ingresar el total de lo que vendió para calcular el porcentaje a pagarle al vendedor, es el 2%
total_de_ventas = int(input("Ingrese el importe total de ventas: "))
# comision= 50 * cVentas
# porcentaje = 0.05 * iTotal
a_pagar = salario + 50 * cantidad_de_ventas + total_de_ventas * 0.05
print("Total a pagar al vendedor", vendedor,"=", a_pagar, "pesos")