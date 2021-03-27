# TP2 ej 8
# Leer un período en segundos e imprimirlo expresado en días, horas, mi-
# nutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7
# horas, 33 minutos y 20 segundos.

periodo = int(input("Ingrese el período en segundos: "))
dias = periodo // (24 * 60 * 60)
periodo = periodo % (24 * 60 * 60)
horas = periodo // (60 * 60)
periodo = periodo % (60 * 60)
minutos = periodo // 60
segundos = periodo % 60
print("")
print("Son en total", dias, "días")
print(horas, "horas")
print(minutos, "minutos")
print("y", segundos, "segundos")