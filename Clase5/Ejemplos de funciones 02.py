# Programación estructurada y modo TOP-DOWN

# Funciones
def mi_funcion(edad, nombre, apellido):
    mensaje = 'Hola cómo estás?'
    edad = int(edad)
    return f'{apellido}, {nombre} tiene {edad} años'  

# Retornará mal el orden de los parámetros

# Código de programa
name = 'Cristina'
age = input('Tu edad ')
ape = input('Tu apellido? ')
salida = mi_funcion(name, age, ape)
print(salida)