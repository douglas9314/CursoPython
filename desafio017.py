# Faça um programa que leia o comprimento do cateto oposto e o cateto 
# adjacente de um triâgulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
print('--== Desafio 017 ==--')
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))
# Forma de fazer utilizando matematica pura
# hi = (co ** 2 + ca **2) ** (1/2)
# Forma de fazer utiliznado math
hi = hypot(co, ca)
print('A hipotenusa é igual a {:.2f}'.format(hi))