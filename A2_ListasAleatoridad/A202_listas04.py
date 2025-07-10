""" Manejo de las listas anidadas.
    El siguiente ejemplo es la manera de entender el concepto
    de las listas anidadas."""
    
    
frutas = ['manzana', 'sandia', 'melon', 'piña', 'durazno', 'uva']
verduras = ['zanahoria', 'cilantro', 'aguacate', 'esparrago', 'champiñon',
             'elote', 'lenteja', 'habas', 'calabaza']

print(frutas)
print(verduras)

# Aquí estamos creando una lista anidada, lista_de_compras contiene dos listas 
lista_de_compras = [frutas, verduras]
print(lista_de_compras)

# Accediendo a los elementos de la lista anidada
print(lista_de_compras[0])
print(lista_de_compras[1])

# Accediendo a los elementos de la primera lista anidada
print(lista_de_compras[0][0])
print(lista_de_compras[0][1])
print(lista_de_compras[0][2])
print(lista_de_compras[0][3])
# accediendo a los elementos de la segunda lista anidada
print(lista_de_compras[1][0])
print(lista_de_compras[1][1])
print(lista_de_compras[1][2])
print(lista_de_compras[1][3])
    
    