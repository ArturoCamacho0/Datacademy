import os

def main():
    op = 1
    while op > 0 and op < 6:

        clear()
        print('*** Bienvenido a los reto de la primera semana! ***\n')
        print('Reto 1: Área del triangulo')
        print('Reto 2: Piedra, papel o tijeras')
        print('Reto 3: Conversor de millas a kilómetros')
        print('Reto 4: Calcular volúmen de figuras')
        print('Reto 5: Rangos cambiantes')
        print('Ingresa cualquier otro número para salir')
        op = int(input('\nIngresa la opción que deseas realizar: '))
        clear()

        if op == 1:
            challenge_01()
        elif op == 2:
            challenge_02()
        elif op == 3:
            challenge_03()
        elif op == 4:
            challenge_04()
        elif op == 5:
            challenge_05()
        
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


def challenge_03():
    while True:
        print('Reto 3: Conversor de millas a kilómetros\n')
        print('1. De millas a kilómetros')
        print('2. De kilómetros a millas')
        print('3. Salir')
        op = int(input('\nIngresa la opción que deseas realizar: '))
        clear()
        if op == 1:
            mi = float(input('Ingresa las millas que quieres convertir: '))
            km = mi * 1.609344
            print('\n')
            print(mi, 'millas equivalen a', km, 'kilómetros.')
        elif op == 2:
            km = float(input('Ingresa los kilómetros que quieres convertir: '))
            mi = km /1.609344
            print('\n')
            print(km, 'kilómetros equivalen a', mi, 'millas.')
        elif op == 3:
            break
        input('\n\nPresiona Enter para continuar...')
        clear()


def challenge_04():
    while True:
        print('Reto 4: Calculadora de volúmenes')
        print('1. Cilindro')
        print('2. Cubo')
        print('3. Esfera')
        print('4. Salir')
        op = int(input('Ingresa la figura que deseas calcuar: '))

        clear()

        if op == 1:
            r = float(input('Ingresa el radio en cm de la base: '))
            h = float(input('Ingresa la altura en cm del cilindro: '))
            A = 3.1416 * (r**2)
            v = A * h
            print('\nEl volúmen del cilindro es de', v, 'cm^3')
        elif op == 2:
            l = float(input('Ingresa el tamaño en cm de un lado del cubo: '))
            v = l**3
            print('\nEl volúmen del cubo es de', v, 'cm^3')
        elif op == 3:
            r = float(input('Ingresa el radio de la esfera: '))
            v = (4/3) * 3.1416 * (r**3)
            print('\nEl volúmen de la esfera es de', v, 'cm^3')
        elif op == 4:
            break

        input('\n\nPresiona Enter para continuar')
        clear()


def challenge_05():
    while True:
        print('Reto 5: Rangos cambiantes\n')
        li = int(input('Ingresa el límite inferior: '))
        ls = int(input('Ingresa el límite superior: '))
        
        while True:
            clear()
            co = int(input('Ingresa el número de comparación: '))

            if co < ls and co > li:
                print(co, 'está dentro de los límites')
                break
            else:
                print(co, 'está fuera de los límites')
                input('Presiona Enter para continuar...')
            clear()
        
        op = int(input('\nIngrese el número 1 para salir o 0 para continuar: '))
        if op == 0:
            clear()
        else:
            break



def clear():
    os.system('clear')

if __name__ == '__main__':
    main()
