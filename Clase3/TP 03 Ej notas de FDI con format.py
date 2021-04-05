"""
El profesor de Fundamentos de Informática necesita una aplicación
que le solicite las dos notas de un alumno, correspondientes al primer
y segundo parcial, y de acuerdo a los datos ingresados informe la situación
del alumno, es decir si: 

Promociona (7 o más de 7 en cada parcial) 
Aprueba la materia (4 o más de 4 en cada parcial) 
Recupera (indicar que parcial, solo puede recuperar un parcial) 
Desaprobado (menos de 4 en ambos parciales)

La aplicación continuará pidiendo notas e informando la situación del alumno
hasta que el profesor escriba "-1" como respuesta a la primer nota.
"""
nota_1 = 0 # Permite entrar al bucle
while nota_1 != -1:
    nombre = input("Ingrese el nombre del alumno: ")
    nota_1 = int(input("Ingrese la primer nota: "))
    # Evalúa la carga solo si nota_1 es distinta de -1
    if nota_1 != -1:
        nota_2 = int(input("Ingrese la segunda nota: "))
        print()
        # usando AND se tienen que cumplir las dos condiciones
        if nota_1 >= 7 and nota_2 >= 7:
            print(f'{nombre} PROMOCIONA la materia con {nota_1} y {nota_2}')
        elif nota_1 >= 4 and nota_2 >= 4:
            print(f'{nombre} APRUEBA la materia con {nota_1} y {nota_2}')
        elif nota_1 < 4 and nota_2 >= 4:
            print(f'{nombre} RECUPERA el primer parcial')
        elif nota_1 >= 4 and nota_2 < 4:
            print(f'{nombre} RECUPERA el segundo parcial')
        else:
            # ninguna de la opciones anteriores
            print(f'Debe recursar la materia')
        print()
print("No hay más alumnos")