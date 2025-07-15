""" Vamos acrear el juego del ahoracado


Inicio --> Generar una palabra  --> generar tantos espacios
           aleatoria                en blanco como tenga la palabra
                                                |
        --<----------<----------------<---------v
        v
        |--------------------------------------------------------------
        V                                                          SI | 
    Preguntar al        Existe la letra   NO                          |
   usuario adivine --> dentro de la     ----> Pierde una vida --> Aun tiene
    una letra           palabra?                                    vidas?
          ^                 | SI                                       |
          |                 V                                          |
          |              Reemplaza el espacio                       NO |
          |             en blanco por la letra                         |
          |                 |                                          |
          |                 V                                          V
          |-----------  Estan todos los espacio -----------------> GAME OVER
                   NO   llenos con las letras?    SI
"""
import random 

# Generar una lista con las posibles palabras a pregunras
lista_palabras = ['casa', 'perico', 'australiano', 'cajita']
palabra = random.choice(lista_palabras)
print(palabra)
# vidas = 6  1.cabeza,          2.Tronco,           3. brazo derecho, 
#            4.brazo izquierdo  5.piena izquierda,  6. pierna derecha
vidas = 6

while vidas > 0:
    letra = input('Proporcione una letra: ').lower()
    if letra in palabra:
        print('Ahi la llevas')
    else:
        vidas -= 1
        print(vidas)
        
    for 
# Por Hacer 1. SEleccionar de la lista de palabras una palabra
# letra = input()

# Por Hacer 2. Preguntar al usuario que adivine una palabra

# Por hacer 3. Verificar si la palbra que el usuairo proporciono
# es correcta o no
