import os

def main():
    op = 1
    while op > 0 and op < 6:

        clear()
        print('*** Bienvenido a los reto de la primera semana! ***\n')
        print('Reto 1: Área del triangulo')
        print('Reto 2: Piedra, papel o tijeras')
        op = int(input('\nIngresa la opción que deseas realizar: '))
        clear()

        if op == 1:
            challenge_01()
        elif op == 2:
            challenge_02()
        
        clear()


def challenge_01():
    print('Reto 1: Área de un triangulo\n')
    b = float( input('Ingresa el valor de la base: '))
    h = float(input('Ingresa el valor de la altura: '))
    A = (b * h) / 2
    clear()

    print('Ahora vamos a determinar el tipo de triangulo!')
    print('-- El lado 3 viene dado por la base que ingresaste --\n\n')
    l1 = float(input('Ingresa la medida del lado 1: '))
    l2 = float(input('Ingresa la medida del lado 2: '))

    if l1 == l2 and l1 == b:
        triangulo = 'Equilatero'
    elif l1 != l2 and l2 != b:
        triangulo = 'Escaleno'
    elif l1 == l2 and l1 != b:
        triangulo = 'Isoceles'
    else:
        triangulo = 'No encontrado'

    print('\nEl área del triangulo', triangulo ,'es', A)
    input('\n\nPresiona Enter para continuar...')


def challenge_02():
    c1 = 0
    c2 = 0

    while True:
        print('Reto 2: Piedra, papel o tijera\n')
        print('-- Elige tu movimiento')
        print('1. Piedra')
        print('2. Papel')
        print('3. Tijeras')
        jugador_1 = int(input('\nJUGADOR 1, ingresa el numero de tu movimiento: '))
        clear()
        print('Reto 2: Piedra, papel o tijera\n')
        print('-- Elige tu movimiento')
        print('1. Piedra')
        print('2. Papel')
        print('3. Tijeras')
        jugador_2 = int(input('\nJUGADOR 2, ingresa el numero de tu movimiento: '))

        clear()

        if jugador_1 == jugador_2:
            pass
        elif jugador_1 == 1 and jugador_2 == 2:
            print('El JUGADOR 2 tiene un punto más!')
            c2 += 1
        elif jugador_1 == 1 and jugador_2 == 3:
            print('El JUGADOR 1 tiene un punto más!')
            c1 += 1
        elif jugador_1 == 2 and jugador_2 == 1:
            print('El JUGADOR 1 tiene un punto más!')
            c1 += 1
        elif jugador_1 == 2 and jugador_2 == 3:
            print('El JUGADOR 2 tiene un punto más!')
            c2 += 1
        elif jugador_1 == 3 and jugador_2 == 1:
            print('El JUGADOR 2 tiene un punto más!')
            c2 += 1
        elif jugador_1 == 3 and jugador_2 == 2:
            print('El JUGADOR 1 tiene un punto más!')
            c1 += 1
        else:
            print('ERROR')

        input('Presiona Enter para coninuar')
        clear()

        print('Jugador 1:', c1, '| Jugador 2:', c2, '\n')

        if c1 == 2 and c2 < 3:
            print('EL JUGADOR 1 HA GANADO!!!')
            print('\nPuntuaje del jugador 1:', c1, 'puntos')
            print('Puntuaje del jugador 2:', c2, 'puntos\n')
            input('Presiona Enter para continuar...')
            clear()
            break
        if c2 == 2 and c1 < 3:
            print('EL JUGADOR 2 HA GANADO!!!')
            print('\nPuntuaje del jugador 1:', c1, 'puntos')
            print('Puntuaje del jugador 2:', c2, 'puntos\n')
            input('Presiona Enter para continuar...')
            clear()
            break

def clear():
    os.system('clear')

if __name__ == '__main__':
    main()
