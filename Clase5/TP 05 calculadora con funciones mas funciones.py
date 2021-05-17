# Calculadora simple con funciones más avanzada

def cargar_numero(orden):
    num = int(input(f'Ingrese el {orden} número: '))
    return num

def menu():
    pass
    while True:
        print(f'Elija 1 ( + ) - 2 ( - ) - 3 ( x ) - 4 ( / ) - 0 (salir):')
        funcion = int(input('Ingrese el número del operador: '))
        if funcion in range(0, 5):
            return funcion

def suma(num1, num2):
    pass
    # Lo hago sin validación
    mas = num1 + num2
    return mas

def resta(num1, num2):
    pass
    # Lo hago sin validación
    menos = num1 - num2
    return menos

def producto(num1, num2):
    pass
    # Lo hago sin validación
    por = num1 * num2
    return por

def division(num1, num2):
    pass
    # Lo hago sin validación
    dividido = num1 / num2
    return dividido

def calcular(op, num1, num2):
    if op == 1:
        print(f'La suma es {suma(num1, num2)}')
    elif op == 2:
        print(f'La resta es {resta(num1, num2)}')
    elif op == 3:
        print(f'El producto es {producto(num1, num2)}')
    elif op == 4:
        if num2 != 0:
            print(f'La división es {division(num1, num2)}')
        else:
            print(f'No se puede dividir por cero!')
    else:
        print(f'No eligió una operación válida')
        
def salir():
    pass
    print()
    print('Gracias por usar la calculadora!')

# BLoque de programa
while True:
    numero1 = cargar_numero('primer')
    numero2 = cargar_numero('segundo')
    opcion = menu()
    if opcion == 0:
        print(f'Salir del programa')
        break
    calcular(opcion, numero1, numero2)
salir()