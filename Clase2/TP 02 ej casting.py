# Casting o "casteo" de variables
"""
El casting es un procedimiento para transformar una variable primitiva de un tipo a otro.
Se le cambia el tipo a la variable durante la ejecución.
type(nombre_de_la_variable) muestra el tipo de variable dada
"""

entrada = input("Ingrese un número: ")
print("Ingresa como:", type(entrada), entrada)
entrada = int(entrada)
print("Con int es:", type(entrada), entrada)
entrada = float(entrada)
print("Con float es:", type(entrada), entrada)
entrada = str(entrada)
print("Y con str se hace:", type(entrada), entrada)