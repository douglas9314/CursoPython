# Faça um programa que leia a largura e a altura de uma parede 
# em metros, calcule a sua área e a quantidade de tinta necessária 
# para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²
print('--== Desafio 011 ==--')
larg = float(input('Digite em metros a largura da parede: '))
alt = float(input('Digite em metros a altura da parede: '))
area = larg * alt
r= area * 0.5
print('É necessario {:.2f} litro(s) de tinta para pintar a parede!'.format(r))