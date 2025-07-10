""" Manejo del simulador del tiro de la moneda."""

import random

cara = random.randint(0, 1)

if cara == 0:
    print('Aguila')
else:
    print('Sol')
