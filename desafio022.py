# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas
# 2. O nome com todas as letras minúsculas
# 3. Quantas letras ao todo
# 4. Quantas letras no primeiro nome
print('--== Desafio 022 ==--')
nome = str(input('Degite seu nome completo: '))
print('Com todas as letras maiúculas {}'.format(nome.upper()))
print('Com todas as letras minúsculas {}'.format(nome.lower()))
print('Quantidade de letras sem espaço: {}'.format(len(nome.replace(' ',''))))
PrimeiraPalavra = nome.split()
print('Quantidade de letras no primeiro nome {}'.format(len(PrimeiraPalavra[0])))