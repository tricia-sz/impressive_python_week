# Operadores in e not in 
# Strings sao ITERAVEIS
# 0 1 2 3 4 5 
# T R I C I A

# nome = 'Trícia'
# print(nome[2])
# print(nome[4])
# print('zero' in nome)
# print('cia' in nome)
# print(10 * '__')
# print('zero' not in nome)
# print('cia' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} NÃO está em {nome}')
