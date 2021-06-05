# Programa que permite cambiar un moneda de un país a dólares

# Las triple comillas permiten crear un cadena de caracteres
# con varias lineas, primero creamos el menú principal
menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

# Escribimos en pantalla el menú y pedimos opción
opcion = input(menu)

# Pesos colombianos a dólares
if opcion == '1':
    # Input para pedir al usuario que ingrese un valor
    pesos = input("¿Cunántos pesos colombianos tienes?: ")
    # float permite cambiar el tipo de datos de string a flotantes
    pesos = float(pesos)
    valor_dolar = 3600
    dolares = pesos / valor_dolar
    # La función round permite redondear una cifra al numero de
    # decimales que escribamos, en este caso dos.
    dolares = round(dolares, 2)
    # str permite pasar a un tipo de datos string
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

# Pesos argentinos a dólares
elif opcion == '2':
    pesos = input("¿Cunántos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 94
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

# Pesos mexicanos a dólares
elif opcion == '3':
    pesos = input("¿Cunántos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 19
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

# Ninguna de las anteriores
else:
    print('Ingresa una opción correcta por favor')