'''
Introducao ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero_string = input('Dobrar o numero que voce digitar: ')

try:
    numero = float(numero_string)
    print(f'O dobro de {numero_string} é {numero * 2:.2f}')
except:
    print('Isso não é um número')