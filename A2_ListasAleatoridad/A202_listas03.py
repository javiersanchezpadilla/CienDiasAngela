""" Errores comunes en el manejo de las listas.
    El error mas comun el IndexError: donde genearalmente
    el valor de referencia del indice queda fuera de la lista
    si tengo 20 alumnos no puedo mencionar al alumno 21 o 40
"""

estados = ['Guerrero', 'Oaxaca', 'Veracruz', 'Jalisco', 'Sonora', 'Chihuahua']

# Pedir a los alumnos como saber la longitud de una lista
print(f'La lisa tiene {len(estados)} elementos disponibles')
print(f'Por lo que los indices van de [0 - {len(estados) - 1}] elementos')

print(estados[0])
print(estados[1])
print(estados[2])
print(estados[3])
print(estados[4])
print(estados[5])

# PEro que sucede si intento acceder al siguiente elemento
# print(estados[6])
#     print(estados[6])
# IndexError: list index out of range