# Faça um algoritmo que leia o preço de um produto e mostre 
# seu novo preço, com 5% de desconto.
print('--== Desafio 012 ==--')
p = float(input('Digite o preço do produto: '))
r = p - (p * 0.05)
print('O novo preço do produto é = {:.2f}'.format(r))