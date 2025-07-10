""" Ejercio de practica, decidir quien hara examen
    En este ejercicio se creara una lista con nombres
    y usando lo que aprendimos de los números aleatorios
    seleccionaremos a uno dentro de la lista
"""
import random


alumnos = ['Carlos', 'Ana', 'Karla', 'Alberto', 'Leticia', 'Isidro']

# Solucion 1 usando una funcion aleatoria sobre la lista
# el alumnos debe investigar sobre una funcio aleatoria que
# actue directemante sobre las listas RANDOM.CHOICE(LISTA)
print('Quien va a presentar el exámen es: ', random.choice(alumnos))

# Solución 2. Creando un índice aleatorio dentro del rango de elemento de la lista
# nuestra lista contiene 6 elemntos por lo que sus indices son desde 0 hasta 5
indice = random.randint(0, 5)
print('El que va a hacer exámen es: ', alumnos[indice])
