""" La sintaxis de If es:
    if condicion:
        haz esto
    else:
        haz esto

    Ejemplos de la vida real
    * Si el nivel de agua de la bañera supera los 80 cm drena el agua
    * Si tu edad es 18 o mas, puedes entrar a ver la pelicula para adultos
    
    OPERADORES RELACIONES O DE COMPARACION
    >   Mayor que           >=  Mayor o igual que 
    <   Menor que           <=  Menor o igual que
    ==  Igual               !=  Diferente o no igual
    
"""

# Desarrollar un programa que evalue para poder subir a la monetaña rusa
# si mides mas de 1.20 Mts

print("Bienvenido a la montaña rusa")
altura = int("cual es tu altura en centimetros? ")

if altura > 120:
    print("Puedes subir a la montaña rusa")
else:
    print("Lo siento debes ser mas alto para poder subir a la montaña rusa")
    