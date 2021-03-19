# Ejercicio Cajero Automático

# Entrada
importeRetirar= int(input("Ingrese Importe a Retirar: "))
# Variables
billetes100 = 0
billetes50 = 0
billetes10 = 0
billetes5 = 0
billetes1 = 0
# Proceso
billetes100 = importeRetirar // 100 # División sin resto
resto = importeRetirar % 100 # Resto de la división

billetes50 = resto // 50
resto = resto % 50

billetes10 = resto // 10
resto = resto % 10

billetes5 = resto // 5
resto = resto % 5

billetes1 = resto // 1
resto = resto % 1

# Salida
print("Billetes a Retirar")
print("------------------")
print("Billetes 100:", billetes100)
print("Billetes 50:", billetes50)
print("Billetes 10:", billetes10)
print("Billetes 5:", billetes5)
print("Billetes 1:", billetes1)
