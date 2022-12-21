# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')
# print(f'O seu nome é {nome=}') # outputa parâmetro + argumento

# numero1 = int(input('Digite um número: '))
numero1 = input('Digite um número: ')
# numero1 = int(input('Digite um número: '))
numero2 = input('Digite outro número: ')
# Linha acima geraria problemas, int() apenas converte dígitos

int_numero_1 = int(numero1)
int_numero_2 = int(numero2)

print(f'A soma dos números é: {numero1 + numero2}') # Será concatenado

