# Calculadora simple con funciones
# Esto es de base, los invito a poner más funciones y hacer que siga haciendo cuentas hasta que salga con 5!

def menu():
    # pass
    print(f'Elija 1 ( + ) - 2 ( - ) - 3 ( x ) - 4 ( / ):')
    # Lo hago sin validación
    funcion = int(input('Ingrese el número del operador: '))
    return funcion # Retorna lo que se asignó en funcion

def suma(num1, num2):
    pass
    # Lo hago sin validación
    mas = num1 + num2
    return mas # Retorna lo que se asignó en mas

def resta(num1, num2):
    pass
    # Lo hago sin validación
    menos = num1 - num2
    return menos # Retorna lo que se asignó en menos

def producto(num1, num2):
    pass
    # Lo hago sin validación
    por = num1 * num2
    return por # Retorna lo que se asignó en por

def division(num1, num2):
    pass
    # Lo hago sin validación
    dividido = num1 / num2
    return dividido # Retorna lo que se asignó en divido

# BLoque de programa
opcion = menu()
numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
if opcion == 1:
    print(f'La suma es {suma(numero1, numero2)}')
elif opcion == 2:
    print(f'La resta es {resta(numero1, numero2)}')
elif opcion == 3:
    print(f'El producto es {producto(numero1, numero2)}')
elif opcion == 4:
    if numero2 != 0:
        print(f'La división es {division(numero1, numero2)}')
    else:
        print(f'No se puede dividir por cero!')
else:
    print(f'No eligió una operación válida')
print()
print('Gracias por usar la calculadora!')
