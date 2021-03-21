# TP2 ej 4
# Ingresar la longitud del radio de un círculo. Calcular e imprimir:

PI = 3.14
radio = int(input("Ingrese el radio del círculo: "))
superficie_circulo = PI * radio**2
perimetro_circunferencia = PI * radio * 2
superficie_esfera = 4 * PI * radio**2
volumen_esfera = (4/3) * PI * radio**3
print("")
print("Los valores calculados para un radio =", radio)
print("-----------------------------")
print("Superficie del círculo =", superficie_circulo)
print("Perímetro del círculo =", perimetro_circunferencia)
print("Superficie de la esfera =", superficie_esfera)
print("Volumen de la esfera =", volumen_esfera)