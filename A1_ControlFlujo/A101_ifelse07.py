""" Manejo de IFs anidados y else

    ESTO ES LO YA RESULTO:
    
    Siguiendo el ejemplo anterior.
    * Si la persona mide 120 cm o mas puede usar la montaña rusa
    * si cumple lo anterior evaluamnos si tiene 18 años paga $12
      si es menor de 18 paga $7, pero si es menor de 12 paga $5
      <12 $5   12 - 18 $ 7   >18 $12
      
    Si el usuario quiere una fotografía se le cobran $3 extra
    
    ESTO SE AUMENTARA 
    Si la persona tiene entre 45 y 55 años no se le cobrara la entrada
"""
print("Bienvenido a la montaña rusa")
altura = int(input("cual es tu altura en centimetros? "))
monto_a_pagar = 0
edad = 0

if altura >= 120:
    print("Puedes subir a la montaña rusa")
    edad = int(input("¿Cuál es tu edad? "))
    
    if edad >= 45 and edad <= 55:
        print("Todo va a ir bien, disfruta un viaje gratis!!!!")
    elif edad > 18:
        monto_a_pagar = 12
    elif edad < 12:
        monto_a_pagar = 5
    else:
        monto_a_pagar = 7
        
    quiere_foto = input("Quiere una fotografia (s/n)? ")
    if quiere_foto == "s":
        monto_a_pagar += 3
        
    print(f"El monto total a pagar es {monto_a_pagar}")
else:
    print("Lo siento debes ser mas alto para poder subir a la montaña rusa")
