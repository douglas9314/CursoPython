# Escreva um programa que convera uma temperatura digitada em 
# ºC e converta para ºF.
print('--== Desafio 014 ==--')
c = float(input('Informe a temperatura em ºC: '))
r = 9 * c / 5 + 32
print('A temperatura de {}º C corresponde a {}º F!'.format(c, r))