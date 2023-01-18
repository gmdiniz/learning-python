'''
while / else

else é alcançado apenas ao fim da execução completa do while, 
se for interrompido não será executado
'''

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i += 1
else:
    print('O else foi executado')