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


# Uso de "f" string
base = 10
altura = 5
print(f'La base = {base}, altura = {altura}')

# Para depuracion en ejcucion
print(f'Valores de las variables {base =} {altura =}')