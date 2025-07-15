""" Vas a escribir un programa que imprima automáticamente la solución 
    al juego FizzBuzz. Estas son las reglas del juego FizzBuzz:
    * Su programa debe imprimir cada número de 1 a 100 a su vez e incluir 
      el número 100.
    * Pero cuando el número es divisible por 3, en lugar de imprimir el número, 
      debería imprimir "Fizz".
    * Cuando el número es divisible por 5, en lugar de imprimir el número 
      debería imprimir "Buzz".`
    * Y si el número es divisible por 3 y 5, p.e. 15 entonces en lugar del número 
      debería imprimir "FizzBuzz"."""
    
for numero in range(1, 101):
    fizz = numero % 3 == 0 and numero // 3 > 0
    buzz = numero % 5 == 0 and numero // 5 > 0
    fizzbuzz = fizz and buzz
    if fizzbuzz:
        print(f'{numero}. FizzBuzz')
    elif fizz:
        print(f'{numero}. Fizz')
    elif buzz:
        print(f'{numero}. Buzz')
    else:
        print(f'{numero}.')
    
print('Fin del ciclo')    
    