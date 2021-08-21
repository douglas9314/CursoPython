# Crie um programa que leia quanto dinheiro uma pessoa tem na 
# carteira e mostre quantos Dolares ela pode comprar.
print('--== Desafio 010 ==--')
n = float(input('Digite o valor em reais: '))
r = n / 3.27
print('É possivel comprar ${:.4f}'.format(r))