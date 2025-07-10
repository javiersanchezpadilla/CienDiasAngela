""" Manejo de numeros aleatorios.

    Explicar el concepto de los módulos, ¿qué son?
    ¿Para que sirven?
    Podemos crear una tarea grande y hacerla todo 
"""

import random

# creamos un valor aleatrorio entero entre 1 y 10
numero_aleatorio = random.randint(1, 10)
print('Número aleatorio entre 1 y 10: ', numero_aleatorio)


# Genera un valor aleatorio flotante entre 0 y 1
print('\nGenerando un valor entre 0 y 1: ', random.random())
# si queremos esta misma tecnica para que nos de un valor entre 0 y 10
print('\nGenerando un valor entre 0 y 10:   ', random.random() * 10)
print('Generando un valor entre 0 y 100:  ', random.random() * 100)
print('Generando un valor entre 0 y 1000: ', random.random() * 1000)


#Podemos uniformar valores flontes en un rango numérico
print('\nValor uniformado flotante entre 1 y 10: ', random.uniform(1, 10))
print('Valor uniformado flotante entre 3 y 5: ', random.uniform(3, 5))


