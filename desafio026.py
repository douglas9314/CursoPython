# Faça um programa que leia uma frase pelo teclado:
# 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a ultima vez
print('--== Desafio 026 ==--')
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes\nPela primeira vez na posição {}\nPela ultima vez na posição {}'
    .format(frase.count('A')
        ,frase.find('A')+1
        ,frase.rfind('A')+1 ))