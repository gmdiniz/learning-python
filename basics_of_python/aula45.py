'''
Iteravel -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
'''

'''
python dunder methods __x__()
'''

# texto = 'Gabriel'
# entregador = iter(texto) # __iter__()
# print(next(entregador))
# print(next(entregador))
# print(next(entregador))
# print(next(entregador))
# print(next(entregador))

# for define um iteravel, solicita o iterador do iteravel, 
# chamando next até o fim do iterador, quando os valores acabarem, 
# uma exception Stopinteration é disparada, 
# indicando ao for para encerrar a iteração

# for letra in texto
texto = 'Gabriel' #iteravel
iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration as error:
        break