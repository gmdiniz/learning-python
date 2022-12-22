'''
Operadores lógicos
and (e) or (ou) not (nao)
and- toda as condições precisam ser verdadeiras,
se qualquer valor for considerado falso, 
a expressão inteira será avaliada naquele valor
São considerados false 
0 0.0 '' False
também existe o tipo None que é 
usado para representar um não valor
'''

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')

print(True and True and True)
