# El objetivo de es ete código es saber si una persona es tiene
# mayoría de edad o es menor de edad.

# Pedimos al usuario su edad
# edad = int(input('Escribe tu edad: '))
# if es el condicional que permite saber si se cumple con una 
# condición, cuando se utilizan condicionales, se termina la 
# línea con dos puntos : y la siguiente línea debe tener una 
# indentación
# if edad > 17:
    # Si se quiere dejar un relleno o un vacío dentro del condicional
    # se coloca pass
    # print('Eres mayor de edad')
# else:
    # print('Eres menor de edad')

numero = int(input('Escribe un número: '))

if numero > 5:
    print('Es mayor a 5')
elif numero == 5:
    print('Es igual a 5')
else:
    print('Es menor a 5')