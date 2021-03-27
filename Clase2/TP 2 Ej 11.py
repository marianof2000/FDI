# TP2 ej 10
# Desarrollar un programa que solicite una temperatura expresada en gra-
# dos centígrados y la imprima convertida a grados Fahrenheit, tal que:
# Calcular para 122 ºF y ver la diferencia de presentación en los datos

# Entrada
temp_farenheit = int(input("Ingrese la temperatura en Farenheit: "))
# Variables y proceso
temp_centigrados = (5 / 9) * (temp_farenheit - 32)
# Salida
print(type(temp_centigrados))
print("Temperatura en Celcius: {:.2f}".format(temp_centigrados))
# Otra forma de formatear
print("Temperatura en Celcius:", round(temp_centigrados,2))