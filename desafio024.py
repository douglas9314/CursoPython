# Crie um programa que leia o nome de uma cidade e diga se ela 
# começa ou não com o nome "SANTO".
print('--== Desafio 024 ==--')
cid = str(input('Em qual cidade você nasceu? ')).strip()
print('A cidade começa com SANTO? {}'.format(cid[:5].upper() == 'SANTO'))