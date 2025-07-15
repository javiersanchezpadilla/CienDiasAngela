""" Proyecto para crear un programa que genere contraseñas.
    1. Debe preguntar cuantas letras quiere para su contraseña.
    2. Preguntas cuantas simbolos quiere dentro de la clave.
    3. Prevuntas cuantos números quiere dentro de la clave.
    
    ESTA PRIMER VERSION ES MUY SENCILLA Y NADA DIFICIL DE QUEBRAR
    PERO SIRVE PARA ENTERNDER LA VESION 2
    La clave la crea el orden y esto es facil de desifrar
    si digo 5 letras, 3 numeros y 5 simbolos, se creará una cadena
    en ese mismo orden LLLLL NNN SSSSS
"""
# Para generar la lista con las letras en mayúsculas y minúsculas
# alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# alfabeto = '!#$%&/()=?¡¨*[];:_,.-{}+¿'
# letras = []
# for letra in alfabeto:
#     letras.append(letra)
# print(letras)    
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

password = ""

for letra in range(0, num_letras):
    password += random.choice(letras)
    
for letra in range(0, num_numeros):
    password += random.choice(numeros)
    
for letra in range(0, num_simbolos):
    password += random.choice(simbolos)
    
print(password)
