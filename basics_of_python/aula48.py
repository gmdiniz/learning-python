'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índice e fatiamento
Métodos úteis: 
    append, adiciona um item ao final 
    insert, adiciona um item no indice escolhido
    pop, remove do final ou do indice escolhido
    del, apaga um indice
    clear, limpa a lista
    extend, estende a lista
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista_a = [1, 2, 3, 4]
lista_b = [5, 6, 7, 8]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

'''
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memoria(mutável)
'''
lista_a = ['Gabriel', 'Joao']
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'