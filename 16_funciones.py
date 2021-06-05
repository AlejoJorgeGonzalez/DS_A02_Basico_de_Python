# Objetivo: Aprender a crear funciones en python

# Para crear una función escribimos la palabra reservada def
# seguido del nombre que queremos de la funciones y terminamos
# con :
# def imprimir_mensaje():
#    print('Mensaje especial: ')
#    print('¡Estoy aprendiendo a usar funciones!')

# Para llamar la función solo tenemos que escribir como se 
# llama, a esto se le llama invocar la función 
#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

# En la funciones esta los parametros que son variables que le
# ingresamos a la función, que para este caso se llama mensaje
def conversacion(mensaje):
    print('Hola')
    print('Cómo estas')
    print(mensaje)
    print('Adios')


opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    # Acá llamamos la funcion conversación y note como se coloca
    # la variable mensaje dentro de los parentesis
    conversacion('Elegistes la opción 1')
elif opcion == 2:
    conversacion('Elegistes la opción 2')
elif opcion == 3:
    conversacion('Elegistes la opción 3')
else:
    print('Escribe la opción correcta')
