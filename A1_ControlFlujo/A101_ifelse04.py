""" Calculadora de IMC con interpretaciones
    Agregue algunas declaraciones if/elif/else a la calculadora de IMC para que interprete 
    los valores de IMC calculados.

    Si el IMC es inferior a 18,5 (sin incluir), imprima "bajo peso"
    Si el IMC está entre 18,5 (incluido) y 25 (sin incluir), imprima "peso normal"
    Si el IMC es 25 (incluido) o más, imprima "sobrepeso"

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

"""

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 25:
    print("overweight")
else:
    print("normal weight")

