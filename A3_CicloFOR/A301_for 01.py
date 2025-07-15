""" Manejo de los ciclos FOR en listas.
        for articulo in lista_de_articulos:
            Haz algo
    
    """
    
# Forma básica de recorrer una lista
for fruta in ['manzana', 'kiwi', 'durazno', 'pera']:
    print(fruta)

    
# Forma dos de recorrer una lista tomando como referencia
# el nombre de la lista    
# las listas son elementos iterables
frutas = ['manzana', 'kiwi', 'durazno', 'pera']

for fruta in ['manzana', 'kiwi', 'durazno', 'pera']:
    print(fruta)
    
# no solo podemos imprimir los valors de una lista 
# podemos ejecutar otras instrucciones
contador_de_frutas = 0
for mi_variable in frutas:
    print('La fruta seleccionada es:', mi_variable)
    contador_de_frutas += 1
    
print('El total de frutas es:', contador_de_frutas)
