# Faça um programa que leia o nome completo de uma pessoa. mostrando 
# o primeiro e o ultimo nome separadamente.
print('--== Desafio 027 ==--')
nome = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}\nSeu ultimo nome é {}'.format(nome[0], nome[len(nome)-1]))