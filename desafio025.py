# Crie um programa que leia o nome de uma pessoa e diga se ela 
# tem "SILVA" no nome
print('--== Desafio 025 ==--')
nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))