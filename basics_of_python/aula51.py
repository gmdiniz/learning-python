'''
Introducao ao desempacotamento
'''

# nome1, *resto = ['Maria', 'Helena', 'Luiz']
_, _, nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)