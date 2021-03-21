# TP2 ej 6
# Leer una medida en metros e imprimir esta medida expresada en centí-
# metros, pulgadas, pies y yardas. Los factores de conversión son:

medida=int(input("Ingrese una medida en metros: "))
centimetros = medida * 100
pulgadas = centimetros / 2.54
pie = pulgadas / 12
yarda = pie / 3
print("")
print("La medida de", medida, "metros equivale a")
print(centimetros, "centímetros")
print(pulgadas, "pulgadas")
print(pie, "pies")
print(yarda, "yardas")