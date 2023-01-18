'''
Calculadora com while
'''

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num1_float = int(numero_1)
        num2_float = int(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
        print(num1_float - num2_float)
    elif operador == '/':
        print(num1_float / num2_float)
    elif operador == '*':
        print(num1_float * num2_float)
    else: 
        ...

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break