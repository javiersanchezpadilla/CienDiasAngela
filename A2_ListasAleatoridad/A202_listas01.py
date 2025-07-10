""" Las listas son estructuras de datos.
    Las estructuras de datos son formas de almacenar
    y estructurar los datos."""
    
# hasta ahora hemos guardado valores a traves de variables
a = 19
nombre = 'Javier'
activo = True

# Pero ¿qué sucede si queremos tener una variable para almacenar
# los estados de la republica? la ultima asignación contendra solo
# el valor, en este caso estado = 'Oaxaca'
estado = 'Guerrero'
estado = 'Veracruz'
estado = 'Oaxaca'

# otra opcion seria crear una variable para cada estado
estado_de_guerrero = 'Guerrro'
estado_de_oaxaca = 'Oaxaca'
estado_de_veracruz = 'Veracruz'
estado_de_jalisco = 'Jalisco'

# Por otro lado imagninemos que tenemos turnos de atención, lo correcto
# es que el primero en formarse sea el primero en atenderse y el último
# que llego sera el último en ser atendido. PAra esto existen las LISTAS
# LAs listas acetpan elementos del mismo tipo o elemento mixtos

estados = ['Guerrero', 'Oaxaca', 'Veracruz', 'Jalisco', 'Sonora', 'Chihuahua']

# Comoe structura de datos debe tener un orden para identificar sus elementos
# para eso existe el control de los índices de cada elemento dentro de la lista
print('Accediendo a los elementos de la lista de forma individual')
print(estados)
print(estados[0])
print(estados[1])

# puedo usar índice negativos, los cuales inician desde el final al inicio
print('\nApuntado a los elementos de la lista con índices negativos')
print(estados[-1])
print(estados[-2])

# Puedo modificar los elementos de la lista
print('\nModificando elementos de la lista')
estados[3] = 'Jalizco'
print(estados)

# Como agregar un elemento a la lista
print('\nAgregando elemento a la lista')
estados.append('Tamaulipas')
print(estados)

# Agregando mas de un elemento dentro de la lista
print('\nAgregando varios elementos a la lista')
estados.extend(['Colima', 'Queretaro', 'Yucatan'])
print(estados)

