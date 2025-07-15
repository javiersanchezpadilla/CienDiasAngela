""" Detereminación del valor mas alto en una lista"""

import random

# lista que genera 50 valores aleatorios
# lista = [ random.randint(100,999) for _ in range(51)]
# print(lista)

lista_valores = [ 592, 248, 849, 195, 194, 280, 733, 177, 608, 798, 478, 858, 723, 
          987, 481, 846, 693, 304, 859, 599, 973, 133, 142, 874, 202, 186, 
          250, 307, 948, 993, 716, 444, 738, 408, 689, 424, 663, 717, 205, 
          381, 391, 938, 222, 498, 881, 300, 404, 484, 955, 497, 389 ]

print(lista_valores)

# Existen una serie de funciones ya especialidas en el manejo de numeros
longitud = len(lista_valores)
suma_total = sum(lista_valores)
valor_maximo = max(lista_valores)
valor_minimo = min(lista_valores)

print('\nVALORES OBTENIDOS MEDIANTE FUNCIONES DE PYTHON')
print('Longitu de la lista:', longitud)
print('Suma total de los valores:', suma_total)
print('El valor máximo:', valor_maximo)
print('El valor minimo:', valor_minimo)

# Ahora realizar estas operaciones mediante un ciclo FOR
longitud_for = 0
suma_for = 0
# Podemos inicializarlo a cero pero su hay negativos puede ser un errir
maximo_for = lista_valores[0]
minimo_for = lista_valores[0]

for dato in lista_valores:
    longitud_for += 1
    suma_for += dato 
    if dato > maximo_for:
        maximo_for = dato
    if dato < minimo_for:
        minimo_for = dato

print('\nVALORES OBTENIDOS MEDIANTE EL CICLO "FOR"')        
print('Longitu de la lista:', longitud_for)
print('Suma total de los valores:', suma_for)
print('El valor máximo:', maximo_for)
print('El valor minimo:', minimo_for)

    