# Programa para entender el funcionamiento de las palabras claves
# continue y break


def run():
    # Se busca imprimir solo los número pares
    #for contador in range(50):
        # El if signica que si el contador divido por 2 da un 
        # valor del modulo diferente de 0 (significa es impar),
        # entra y con el continue termina inmediatamente este 
        # ciclo para que el for comienze nuevamente. 
        # if contador % 2 != 0:
        #     continue
        # print(contador)

    # for i in range(1000):
    #     print(i)
        # Si la variable i llega a ser 20, se activa el break 
        # el cuál termina inmediatamente el for
        # if i == 20:
        #     break
    

    # El objetivo es parar el ciclo for apenas se encuentre la 
    # letra 'o'
    texto = input('Escribe un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()
