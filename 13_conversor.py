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