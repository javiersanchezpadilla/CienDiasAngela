""" Realizar el siguiente programa para calcular de una cuenta de una 
    comida cuanto tiene que pagar cada uno d ellos """
    
    
print("Bienvenido a la calculadora de propina!")

total_cuenta = float(input("Cuanto es el total de la cuenta? "))
porcentaje_propina = int(input("Cuanta propina quieres dar? (10, 12, o 15)? "))
personas = int(input("En cuantas personas se divirá la propina? "))

monto_individual = (total_cuenta * ( 1 + porcentaje_propina / 100)) / personas

print(f'Cada persona debe pagar ${round(monto_individual, 2)}')
