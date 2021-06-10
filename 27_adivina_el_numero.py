# Se utiliza módulos, los módulos de python son códigos 
# que los mismos desarrolladores de python han realizado para
# nosotros, son funciones que permiten ahorrar tiempo y trabajo 
# en la escritura de nuestro código, para llamarlos usamos la 
# palabra reservada import
# El módulo ramdom es el diseñado para funciones de aleatoriedad
import random


def run():
    # random.randint da un número entero aleatorio entre un 
    # rango, que para este caso es de 1 al 100
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run() 