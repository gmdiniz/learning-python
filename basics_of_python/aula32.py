'''
1- Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro.
'''

str_number = input('Digite um número inteiro: ')
try: 
    number = int(str_number)
    is_par = number % 2 == 0
    if is_par:
        print('O número é par')
    else: 
        print('O número é ímpar')
except:
    print('O número não é um inteiro')

'''
2- Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

hora = input('Digite a hora atual: ')
try:
    hora_int = int(hora)
    if hora_int in range(0, 11):
        print('Bom dia')
    elif hora_int in range(12, 17):
        print('Boa tarde')
    elif hora_int in range(18, 23):
        print('Boa noite')        
except:
    print('Digite uma hora válida')


'''
3- Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva 'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva
'Seu nome é normal'; maior que 6 escreva 'Seu nome é muito grande'.
'''

nome = input('Digite seu primeiro nome: ')

if not nome.isdigit:
    tamanho_nome = len(nome)
    if tamanho_nome >= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 or tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
else:
    print('Digite uma string')
