"""
Formatacao basica de strings

s - strings
d - int
f - float
.<numero de difitos>f
x ou X - Hexadecimal
(caractere) (><^)(quantidade)
> - Esquerda
> Direita
^ centro
Sinal + ou -
Ex.: 0>-100. .1f
Converion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.') 
print(f'{1000.54566547654546:.1f}')
print(f'{1000.54566547654546:,.1f}')
