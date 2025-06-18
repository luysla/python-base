#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10

Modelo:

---Tabuada do 1---
1 x 1 = 1
1 x 2 = 2
...
###################

---Tabuada do 2---
2 x 1 = 2
2 x 2 = 4
...
"""
__version__ = "0.0.1"
__author__ = "Luysla Dyana"

numeros = list(range(1, 11))

for n1 in numeros:
  print("{:-^18}".format(f"Tabuada do {n1}"))
  print()
  for n2 in numeros:
    resultado = n1 * n2
    operacao = f"{n1} x {n2} = {resultado}"
    print("{:^18}".format(operacao))
  print("#" * 18)
