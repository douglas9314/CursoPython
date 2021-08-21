# Crie um programa que leia um numero Real qualquer pelo teclado e 
# mostre na tela a sua porção inteira.
from math import trunc
print('--== Desafio 016 ==--')
n = float(input('Digite um numero: '))
# forma de fazer usando apenas o metodo int
# print('A porção inteira do numero {} é igual a {}',format(n,int(n)))
# forma usando o math
print('A porção inteira do numero{} é igual a {}'.format(n,trunc(n)))

