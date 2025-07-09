""" podemos manipular la presentación de los resultados."""

# Manejo del redondeo de los datos
print('Redondeo de valores')
valor = 3.563337
print(valor)
print(int(valor))
print(round(valor))
print(round(valor, 2))
print(round(valor, 5))

print("El valor de la variable valor =", str(valor))
# manejo de f-string ya no se requieren conversiones de ningun tipo
print(f'El valor de la variable valor = {valor}')

altura = 1.8
peso = 80.5
puntaje = 0
esta_ganando = True

print("\nDatos mostrados de forma tradicional")
print("Altura:", str(altura))
print("Peso:", str(peso))
print("Puntaje:", str(puntaje))
print("Esta ganando:", str(esta_ganando))



print("\nDatos mostrados mediante f-string")
print(f"Altura: {altura}")
print(f"Peso: {peso}")
print(f"Puntaje: {puntaje}")
print(f"Esta ganando: {esta_ganando}")

