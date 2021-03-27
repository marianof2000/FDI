# TP2 ej 10
# Un banco necesita para sus cajeros automáticos un programa que lea
# una cantidad de dinero e imprima a cuántos billetes equivale, conside-
# rando que existen billetes de $100, $50, $10, $5 y $1. Desarrollar dicho
# programa de tal forma que se minimice la cantidad de billetes entrega-
# dos por el cajero.

# Entrada
importe_a_retirar= int(input("Ingrese Importe a Retirar: "))
# Variables
billetes_100 = 0
billetes_50 = 0
billetes_10 = 0
billetes_5 = 0
billetes_1 = 0
# Proceso
billetes_100 = importe_a_retirar // 100 # División sin resto
resto = importe_a_retirar % 100 # Resto de la división
billetes_50 = resto // 50
resto = resto % 50
billetes_10 = resto // 10
resto = resto % 10
billetes_5 = resto // 5
resto = resto % 5
billetes_1 = resto // 1
resto = resto % 1
# Salida
print("Billetes a Retirar")
print("------------------")
print("Billetes 100: ", billetes_100)
print("Billetes 50: ", billetes_50)
print("Billetes 10: ", billetes_10)
print("Billetes 5: ", billetes_5)
print("Billetes 1: ", billetes_1)