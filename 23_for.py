# Programa para aprender como funciona el ciclo for

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# contador = 1
# print(contador)
# while contador < 20:
#     # contador = contador + 1 se puede reemplazar por
#     contador += 1
#     print(contador)

# Función range crea una sucesión números desde 0 hasta el valor
# especificado
# a = list(range(20))
# print(a)


# el for va a crear una variable llamada contador que va desde
# rango (range) desde 1 hasta 0. Note que el range tiene dos 
# valores (1, 21) para poder comenzar desde 1, porque si solo
# tuviera un valor, el range empieza desde 0, además el range 
# llega hasta el valor anterior al que se le especifica, es este
# caso llega hasta 20 
for contador in range(1, 21):
    print(contador)

for i in range(10):
    print(11 * i)
