""" Los tipos de datos primitivos de python son
    int, float, str, bool
    
    El encadenamiento tiene que ver con la union de letras podemos extrar 
    cualquier caracter dentro del corchete podemos colocar la posicion 
    del caracter que queremos extraer
    """

# el método a usar se denomina uso de corchetes para extraer un caracter    
print("Hola a todos"[0])
print("Hola a todos"[1])
print("Hola a todos"[2])

# Qué pasa si queremos extraer el último caracter de la palabra?
print("El último caracter de la palabra es:","Hola a todos"[11])

# podemos usar un truco mediante el uso de índices negativos
print("El último caracter de la palabra es:","Hola a todos"[-1])

# Entender el uso de las cadenas ¿Cuál será el resultado?
# el resultado del comportamiento de la suma es concatenación
print("123" + "45678")

# Si queremos que el comportamiento sea distinto tenemos que manejar
# los valores como numeros y no como cadenas
print(123 + 100)

# En lugar del uso de comas python nos permite el uso de guiones bajos
print(123_000 + 100_000)
mystery = 734_529.678
print(mystery)

# Tipo de dato flotate o punto flotante
print(3.1415927)
print(31.415927)
print(314.15927)
print(3141.5927)
print(31415.927)

# Tipo de dato flotante, solo tiene dos valores True o False
print(True)
print(False)