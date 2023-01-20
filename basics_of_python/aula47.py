'''
Faça um jogo par o usuario advinhar qual 
a palavra secreta.
- Voce vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuario digitar apenas uma letra.

- Quando o usuario digitar uma letra, voce 
vai conferir se a letra digitada está na palavra secreta.
    - se a letra digitada estiver na 
    palavra secreta; exiba a letra;
    - se a letra digitada nao estiver 
    na palavra secreta; exiba *.

Faça a contagem de tentativas de seu
usuario.
'''

import os

segredo = 'amendoim'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in segredo:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra in segredo:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    
    if palavra_formada == segredo:
        os.system('clear')
        print('Voce ganhou')
        print('Segredo é, ', segredo)
        print('Tentativas, ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
