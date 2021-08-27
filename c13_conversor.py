# Programa que permite cambiar un moneda de un país a dólares

# Es una buena practica colocar las funciones en la parte superior
# antes de comenzar con el código principal, para que cuando python
# las tenga lista antes de ser llamadas
# Conversor realiza la conversión de una moneda a dolares, esta 
# compuesta por dos parametros: tipo_pesos que el nombre del peso
# a calcular y valor_dolar que es el valor de la moneda americana
# en el momento de calcular
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

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
    # Llamamos a la función conversor 
    conversor('colombianos', 3600)
# Pesos argentinos a dólares
elif opcion == '2':
    conversor('argentinos', 94)
# Pesos mexicanos a dólares
elif opcion == '3':
    conversor('mexicanos', 19)
# Ninguna de las anteriores
else:
    print('Ingresa una opción correcta por favor')