# Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
# do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians
print('--== Desafio 018 ==--')
angulo = radians(float(input('Digite um âlgulo qualquer: ')))
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)
print('SENO = {:.2f}\nCOSSENO = {:.2f}\n TANGENTE = {:.2f}'.format(seno, cosseno, tangente))

