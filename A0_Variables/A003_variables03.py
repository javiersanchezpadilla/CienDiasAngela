""" Ejercicio, capturar un nombre y determinar cuantos caracteres contiene el nombre
    javier = 6, Ada = 3, Alberto = 7 
    Recordar que contamos con google --> longitud de una cadena python
    debemos pensar no acumular               P e t i c i o n    lenguaje
    """
    
print(len(input('¿Cuál es tu nombre?')))

# Ahora desglozara lo anterios y el nombre asignarlo a una variable 
# y la longitud del nombre almacenarlo en otra variable
nombre = input('Dame tu nombre ')
longitud = len(nombre)
print(longitud)

# Pero como ya sabemos usar cadenas podemos decorarla un poco
print('La longitud del nombre', nombre, 'es', longitud )