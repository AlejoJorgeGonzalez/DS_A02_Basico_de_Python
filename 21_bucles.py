# Programa para obtener las potencias de 1

# contador = 0
# print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(2**contador))

# contador = 1
# print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(2**contador))

# contador = 2
# print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(2**contador))

# contador = 3
# print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(2**contador))

# contador = 4
# print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(2**contador))

# contador = 5
# print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(2**contador))


def run():
    # Se define un limite hasta donde va a llegar el resultado
    # de las potencias de 2, cuando se van a colocar constantes
    # se utiliza el nombre con letras máyusculas
    LIMITE = 1000000
    # contador va a ser el número de la potencia 
    contador = 0
    pontencia_2 = 2**contador

    # El while funciona con una condición, que mientras se cumple
    # va a repetir los pasos dentro del while
    while pontencia_2 < LIMITE:
        print('2 elevado a ' + str(contador)+ ' es igual a: ' + str(pontencia_2))
        # Se realiza el cambio de condiciones para que en un 
        # momento dado se pueda salir del while y no entremmos 
        # un infinity loop
        contador = contador + 1
        pontencia_2 = 2**contador


if __name__ == '__main__':
    run()