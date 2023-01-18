frase = 'O python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido van Rossum.'.lower().strip()

i = 0
letra_mais_frequente = ''
maior_frequencia = 0

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue

    frequencia = frase.count(letra_atual)

    if frequencia > maior_frequencia:
        letra_mais_frequente = letra_atual
        maior_frequencia = frequencia

    i += 1
    
print('A letra mais frequente é: ' f'{letra_mais_frequente}' ', e apareceu' f'{frase.count(letra_mais_frequente)}x')
