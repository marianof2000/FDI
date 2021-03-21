# TP2 ej 5
# Escribir un programa que permita ingresar la edad de una persona en
# años y la convierta a días, imprimiendo el resultado. Considerar que to-
# dos los años tienen 365 días.

DIAS_ANIO = 365
edad = int(input("Ingrese su edad en años: "))
edad_dias = DIAS_ANIO * edad
print("")
print("Su edad en días es =", edad_dias)