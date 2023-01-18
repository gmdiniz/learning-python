'''
Iterando strings com while
'''

nome =  'Gabriel Diniz Mota'
tamanho_nome = len(nome)

iterador = 0
novo_nome = ''
while iterador < tamanho_nome:
    letra = nome[iterador]
    novo_nome += f'*{letra}*'
    iterador += 1

