""" Uso de entrada de datos
    En este ejercicio se entendera:
    1. la importancia de poder interactura con el ususario, es necesaria
       una funcion de entrada de datos.
    2. Como usar una funcion dentro de otra funcion print( input())  """


# Evolucion, que pasa si queremos personalizar un saludo, 
# realmente tendriamos que adivinar a quien va dirigido el saludo
print('Hola, ¿cuál es tu nombre?')
print('Bienvenido Javier')

# podemos reemplazar el print por una funcion de entrada, la entrada 
# de datos es recibida por la funcion input pero no hay maneara de 
# recuperar el dato capturado mediante el teclado.
input('Hola, ¿cuál es tu nombre? ')

# Podemos mezclar ambas instrucciones, aqui una vez que se ejecuta 
# el input continua la ejecución de la funcion print
print('Hola Bienvenido ' + input('Hola, ¿cuál es tu nombre? '))

# Como reto podemos pedir al usuario crear un mensaje personalizado 
# donde se pida el nombre del usuario y se salude, pero al final 
# imprimir signos de admiración
print('Hola Bienvenido ' + input('Hola, ¿cuál es tu nombre? ') + '!!!!!!')