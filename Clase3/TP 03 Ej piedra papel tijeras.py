'''Piedra, Papel o Tijeras 
Se debe realizar el programa para jugar 5 rondas de 3 juegos cada una, de piedra, papel o tijera. 
Juega un usuario contra la máquina. Se debe indicar el resultado del campeonato al terminar las 5 rondas.
Los elementos son: Piedra, Papel o Tijeras
El usuario elije uno de los elementos. 
La máquina elije luego de manera aleatoria. 
Se analiza cada jugada y se indica quien ganó en cada caso, informando luego el ganador de cada juego.
En caso de empate, se indica, pero no se computa el juego, debe repetirse.
'''
import random

puntos_pc = 0
puntos_jug = 0
ronda_pc = 0
ronda_jug = 0
rondas = 0
juegos = 0
nombre = input('Me decís tu nombre? ')
print()
while rondas < 5:
    rondas += 1
    print(f'Ronda {rondas}')
    while juegos < 3:
        juegos += 1
        jugada_pc = random.randint(1,3)
        jugada_jug = int(input('1-Piedra / 2-Papel / 3-Tijeras '))
        while jugada_jug < 1 or jugada_jug > 3:
            print(f'Debe elegir 1, 2 ó 3')
            jugada_jug = int(input('1-Piedra / 2-Papel / 3-Tijeras '))
            print()
        # print(f'{jugada_pc}')
        if jugada_jug == jugada_pc:
            print('Empate!!')
            juegos -= 1
        # Uso de "\" para bajar de línea
        elif (jugada_jug == 1 and jugada_pc == 2)\
            or (jugada_jug == 2 and jugada_pc == 3)\
            or (jugada_jug == 3 and jugada_pc == 1):
            print(f'{nombre} gané esta mano!!')
            ronda_pc += 1
        else:
            print(f'{nombre} me ganaste esta mano!!')
            ronda_jug += 1
        print()
    print(f'Fin del juego {rondas}')
    print()
    juegos = 0
    if ronda_pc > ronda_jug:
        puntos_pc += 1
    elif ronda_pc < ronda_jug:
        puntos_jug += 1
if puntos_pc > puntos_jug:
    print(f'{nombre} lamento decirte que te gané {puntos_pc} de 5')
elif puntos_pc < puntos_jug:
    print(f'{nombre} te felicito, me has ganado en {puntos_jug} de 5!!')
else:
    print(f'{nombre} hubo un empate. Gracias por jugar')