""" Crear un generador de nombres de bandas.
    Proporcionamos la ciudad donde nacimoa
    Seguido del nombre de la mascota
    Com oresultado el nombre propuesto sera
    el nombre de la ciudad mas el nombre de la mascota"""

print('Bienvenido al generador de nombres de bandas')
ciudad = input('En que ciudad naciste? ')
print(ciudad)
mascota = input('Cual es el nombre de tu mascota? ')
print('El nombre de tu mascota puede ser: ' + ciudad + " " + mascota)
