import os

def main():
    os.system('clear')
    print('*** Bienvenido a los reto de la primera semana! ***\n')
    print('Reto 1: Área del triangulo')
    op = int(input('\nIngresa la opción que deseas realizar: '))
    os.system('clear')

    if op == 1:
        challenge_01()
    
    os.system('clear')

def challenge_01():
    print('Reto 1: Área de un triangulo\n')
    b = float( input('Ingresa el valor de la base: '))
    h = float(input('Ingresa el valor de la altura: '))
    A = (b * h) / 2
    print('\nLa altura del triangulo es', A)
    input('\n\nPresiona Enter para continuar...')

if __name__ == '__main__':
    main()
