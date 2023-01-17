'''
Exercicio
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade 
Se o nome e idade forem digitados:
    Exiba:
        Seu nome e {nome}
        Seu nome invertido e {nome invertido}
        Seu nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        'Desculpe, você deixou campos vazios.'
'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if not nome and not idade:
    print('Desculpe, você deixou campos vazios.')
else: 
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else: 
        print(f'Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A primeira letra do seu nome é: {nome[-1]}')
