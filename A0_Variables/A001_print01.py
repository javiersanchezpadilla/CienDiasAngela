""" En este código comprenderemos el uso de print."""

# Podemos usar print con comilla simple o comilla doblre
print("Hola a todos")
print('Hola a todos')

# Segmentos de texto dentro de un print
print('Hola', 'Esta es', 'otra forma del', 'uso de print')

# podemos imprimir varias lineas mediante el carrie return \n
print('Esta es\nuna linea\npartida en cuatro\npartes')

# Concatenacion de cadenas
print('Hola' + ' a ' + 'todos ' + 'esta es ' + 'una linea' + " concatenada" )

# Manejo del redondeo de los datos
print('Redondeo de valores')
valor = 3.563337
print(valor)
print(int(valor))
print(round(valor))
print(round(valor, 2))
print(round(valor, 5))

# uso de barra inversa para continuar la linea en otra mas
print(f'Esto permite '\
    f'que continuemos {2+3} el'\
        f' el uso del fstring')

print('Tambien podemos \
Hacer uso de la contrabarra\
 para partir una liena')

# podemos tambien continuar una liena de la siguiente manera
print('Podemos simplemente continuar la liena abriendo y cerrando dentro de la misma funcion')
print('Esta es una '
      ' linea larga'
      ' larga dividida en varias lineas')


# Uso de "f" string
base = 10
altura = 5
print(f'La base = {base}, altura = {altura}')

# Para depuracion en ejcucion
print(f'Valores de las variables {base =} {altura =}')

# Impresion multilinea (puede ser con comilla doble o simple)
print(""" 
 _           _                         
| |         | |                        
| |__   __ _| |_ _ __ ___   __ _ _ __  
| '_ \ / _` | __| '_ ` _ \ / _` | '_ \ 
| |_) | (_| | |_| | | | | | (_| | | | |
|_.__/ \__,_|\__|_| |_| |_|\__,_|_| |_|
""")

# Escapar caracteres o simplemente imprimir comillas dentro de los mensajes
# si vamos a usar comillas dobles dentro del texto  usamos comilla simple
# para envolver el texto y a la inversa
print('la cancion se llama "Smells Like Teen Spirit"')
print("La cancion de llama 'Smells Like Teen Spirit'")

# tambien podemos escapar los simbolos con la contrabarra
print('La cancion se llama \'Smells Like Teen Spirit\'')
print("La cancion se llama \"Smells Like Teen Spirit\"")

