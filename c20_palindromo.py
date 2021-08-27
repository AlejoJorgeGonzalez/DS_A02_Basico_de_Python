# Programa que permite saber si una palabra o frase es 
# palindromo


def palindromo(palabra):
    # Primero se elimina los espacios que de pronto tenga una 
    # frase, ya que python toma los espacios como caracteres, 
    # pero la definición de palíndromo no toma estos espacios
    palabra = palabra.replace(' ', '')
    # lower convierte todos los caracteres en mínusculas
    palabra = palabra.lower()
    # Se inverte la palabra
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


# Por buenas practicas es recomendable que se comience un programa
# por medio de una función, en este caso se le puede cambiar el 
# nombre, pero se utiliza run que es una palabra muy utilizada en
# sector
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')
# Es buena practica dejar dos espacios entre funciones


# Se coloca el entry point, o punto de entrada en python, siempre
# se tiene que colocar de esta forma. Es muy buena practica que
# todo programa tenga este punto de entrada, porque python lo 
# primero que busca es este punto de entrada
if __name__ == '__main__':
    # Python va a buscar la función run, que esta declarada arriba
    # y ejecutarla
    run()