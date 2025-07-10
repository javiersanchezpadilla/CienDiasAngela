""" En este programa simularemos el juego de piedra, papel o tijera
    Descargar desde ASCII Art las imagenes para cada una de ellas
    <0> Piedra  <1> Papel  <2> Tijera
    piedra gana tijera, papel gana piedra, tijera gana papel
      0          2       1        0           1       1    
      
    Las imagenes son variables con ASCII Art, dentro de una lista
    1. primero hacer el programa sin usar OR's y despues hacer la version
       usando los OR's
"""
import random

piedra = '''
    _______
___|   ____)_
       (_____)
       (_____)
       (____)
---.__(___)       
'''

papel = '''
    _______
___|   ____)_____
         ________)
        __________)
       __________)
---.___________)       
'''

tijera = '''
   _______
___|   ____)_____
         ________)
       ___________)
       (____)
---.__(___)       
'''

imagenes_juego = [piedra, papel, tijera]

print('JUEGO DE PIEDRA, PAPEL O TIJERA\n\n')


humano = int(input('<0> Piedra, <1> Papel o <2> Tijera'))

# Se valida la opción que sea válida solo se acepta (0, 1, 2)
if humano < 0 or humano > 2:
    print('ERROR! opcion no valida para el juego')
else:
    # Si es una opción valida inicia el juego
    computadora = random.randint(0, 2)

    print(f'Tu elección: {humano}')
    if humano == 0:
        print('PIEDRA')
    elif humano == 1:
        print('PAPEL')
    else:
        print('TIJERA')
    print(imagenes_juego[humano])

    print(f'La computadora: {computadora}')
    if computadora == 0:
        print('PIEDRA')
    elif computadora == 1:
        print('PAPEL')
    else:
        print('TIJERA')
    print(imagenes_juego[computadora])

    # Analisis del juego
    if computadora == humano:
        print('Es un empate!!!!')
    elif (humano == 0 and computadora == 2) or (humano == 1 and computadora == 0) or (humano == 2 and computadora == 1):
        print('Tu ganas!!!')
    elif (computadora == 0 and humano == 2) or (computadora == 1 and humano == 0) or (computadora == 2 and humano == 1):
        print('Tu pierdes!!!!')
    else:
        print('Opción incorrecta!!!!')
    