""" Manejo de rangos en los ciclos.
    Es importante notar que en el manejo de los rangos el 
    limite superior no es inclusivo, esto quiere decir que
    un ciclo con un rango hasta 10 considerará diez valores
    pero desde 0 (valor 1), hasta 9 (valor 10)"""

# imprime los valores entre 0 y 4
print('\nEjemplo 01 uso de range normal de 0 a limite-1')
for numero in range(5):
    print(numero)

# si queremos que en valor 5 sea incluido desde 0 a limite+1
print('\nEjemplo 02 uso de range de 0 a limite+1')
for numero in range(6):
    print(numero)

# queremos rangos que no inicien desde 0 rango de 5 a 10 (limite+1)
print('\nEjemplo 03 uso de range desde un valor_inicial a limite')
for numero in range(5, 11):
    print(numero)
    
# queremos rangos que no inicien desde 0 y que tenga saltos
print('\nEjemplo 04 uso de range desde un valor_inicial a limite con saltos de 3')
for numero in range(5, 16, 3):
    print(numero)

# ciclos con rangos decrementales
print('\nEjemplo 05 uso de range decrementando desde -5 hast -10 decrementando -1')
for numero in range(-5, -10, -1):
    print(numero)

# ciclos con rangos decrementales con saltos distintos a -e
print('\nEjemplo 05 uso de range decrementando desde -5 hast -10 decrementando -1')
for numero in range(-5, -20, -3):
    print(numero)


