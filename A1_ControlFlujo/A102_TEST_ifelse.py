""" Para probar el uso de los condicionantes vamos a desarrollar una especia
    de juego en el cual tomaremos dicisiones 
    1. Inicio del juego
    2. si el usuario va a la derecha el juego termina, a la izq. continua
    3. Si el ususario decide nadar el juego termina (cocodrilos) si decide
       esperar continua.
    4. si el usuario elige la puerta roja el juego termina, si elije la
       puerta azul el juego termina, y si elije la puerta amarilla gana el tesoro
    """
    
   
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************      
''')

print('Bienvenido a la isla del tesoro')
print('Tu misión es encontrar el tesoro')

# En esta captura explicar las variantes izq IZQ Izq, etc. por lo que se recomienda lower()
opcion1 = input('Te encuentras en un camino cruzado, ¿a donde quieres ir? '
                '(escribe izquierda o derecha) ').lower()

if opcion1 == "izquierda":
    opcion2 = input('Llegaste a un lago y hay una isla a la mitad del lago, '
                    'teclear "nadar" para llegar hacia la isla, o teclear '
                    '"esperar" para esperar un bote. ').lower()
    if opcion2 == "esperar":
        opcion3 = input('llegaste a la isla desarmado. Llegaste a una casa donde hay'
                        'tres puertas una "azul", una "roja" y la otra "amarilla"'
                        'Que color elijes?').lower()
        if opcion3 == 'roja':
            print('Es un cuarto lleno de fuego. PERDISTE!!!')
        elif opcion3 == 'amarilla':
            print('Encontraste el tesoro, FELICIDADES HAS GANADO!!!!')
        else:
            print('Encontraste un cuarto lleno de animales salvages. PERDISTE!!!!')
    else:
        print('Te ahogaste, PERDISTE!!!!')
else:
    print('Caiste en un pozo. Juego terminado')
