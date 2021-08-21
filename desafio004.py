# Faça um programa que leia algo pelo teclado e mostre na tela 
# o seu tipo primitivo e todas as informações possiveis sobre ele.
print('--== Desafio 004 ==--')
a = input('Digite algo: ')
print('O tipo primitivo de valor é {}'.format(type(a)))
print('So tem espaço ? {}'.format(a.isspace()))
print('É um numero ? {}'.format(a.isnumeric()))
print('É alfabético ? {}'.format(a.isalpha()))
print('É alfanumerico ? {}'.format(a.isalnum()))
print('É maiusculo ? {}'.format(a.isupper()))
print('É minusculo ? {}'.format(a.islower()))
print('Está capitalizada ? {}'.format(a.istitle()))