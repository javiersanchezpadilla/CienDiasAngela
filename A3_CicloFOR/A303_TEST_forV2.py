""" Proyecto para crear un programa que genere contraseñas.
    1. Debe preguntar cuantas letras quiere para su contraseña.
    2. Preguntas cuantas simbolos quiere dentro de la clave.
    3. Prevuntas cuantos números quiere dentro de la clave.
    
    EN ESTA SEGUNDA VERSION SE HACE DINAMICA LA POSICION DE LOS
    CARACERES DE LA CONTRASEÑA, ESTO ES, UAN VEZ CREADA LA CONTRASEÑA
    VAMOS A MEZCLARLOS ENTRE SI.
    Los alumnos deberán buscar en internet como mezclar los elementos
    de una lista en python
    """

import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
          'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¡', '¨', '*', '[', ']', ';', ':', '_', ',', '.', '-', '{', '}', '+', '¿']

print('Bienvenido al generador de contraseñas de Python')
print('\nDATOS REQUERIDOS PARA LA CREACIÓN DE LA CONTRASEÑA')

num_letras = int(input('¿Cuantas letras debe contener? '))
num_numeros = int(input('¿Cuantos números debe contener? '))
num_simbolos = int(input('¿Cuantos simbolos debe contener'))

# Ahora manejaremos la clave como una lista
password_list = []

for letra in range(0, num_letras):
    password_list.append(random.choice(letras))
    
for letra in range(0, num_numeros):
    password_list.append(random.choice(numeros))
    
for letra in range(0, num_simbolos):
    password_list.append(random.choice(simbolos))
    
# ya tenemos una lista con los caracteres 
print(password_list)

# Ahora vamos a desordenas los elementos de la lista
random.shuffle(password_list)
print(password_list)

# ya tenemos una lista mezclada, ahora vamos a crear una cadena
# METODO 1
password_cadena = ''
for letra in password_list:
    password_cadena += letra

print(password_cadena)

