""" Problema para el uso de casteo
    Vamos a arreglar este problema y hacerlo mas legible
    print(len(input('Dame tu nombre: ')))
"""
# el primer paso es desglozar en variables para hacer mas sencillo de entender
nombre_del_usuario = input('Introduce tu nombre: ')
longitud_de_nombre = len(nombre_del_usuario)

print(type('Numero de letras en tu nombre'))
print(type(longitud_de_nombre))

print('Numero de letras en tu nombre: ' + str(longitud_de_nombre))


