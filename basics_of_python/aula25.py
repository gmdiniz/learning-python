'''
Interpola ção básica de string
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF01234567)

- f strings
- format
- interpolação

'''

nome = 'Gabriel'
preco = 1000.39459
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexa de %d é %08X' % (1500, 1500))



