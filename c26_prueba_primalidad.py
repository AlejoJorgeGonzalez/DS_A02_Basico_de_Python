# Programa para saber si un número es primo o no

def es_primo(numero):
    contador = 0

    # El range va hasta el numero anterior que se escribe, por
    # tanto se debe agragar el +1 para poder llegar al número 
    # solicitado
    for i in range(1, numero + 1):
        # Si i es igual a 1 o el número que ingrese al usario,
        # simplemente no realiza ninguna acción en este ciclo y
        # se pasa al siguiente, porque ya sabemos que un número
        # es divisible por 1 y por su propio número
        if i == 1 or i == numero:
            continue

        # Si la división del número con i, es una división exacta
        # el contador se suma una unidad
        if numero % i == 0:
            contador += 1
    
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe un número: '))
    # Observese que el if no tiene una comparación, python 
    # permite tener una variable o función sin una comparación
    # o prueba lógica si esta variable es un booleano o la 
    # función devuelve un booleano. El if se ejecuta si es True
    # o no se ejecuta si el False  
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
