# Escreva um programa que leia um valor em metros e o exiba 
# convertido em centimetros e milimetros.
print('--== Desafio 008 ==--')
metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000 
print('Comprimento em centimetros é igual a {:.2f}, e em milimetros é igual a {:.2f}'.format(centimetros, milimetros))  