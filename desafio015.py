# Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa 
# R$0,15 por KM rodado.
print('--== Desafio 015 ==--')
km = float(input('Digite a quantidade de Km percurridos: '))
dias = int(input('Digite a quantidade de dias foi alugado: '))
r = km * 0.15 + dias * 60
print('O preço a pagar é R${:.2f}'.format(r))
