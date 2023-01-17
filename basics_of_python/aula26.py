'''
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X hexadecimal
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr__  __str__ __ascii__
'''
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{10000000.343433443:.1f}')