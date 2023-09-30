"""
Interpolacao basica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF01123456789)
"""

nome = 'Tricia'
preco = 1000.95897643
variavel = '%s, o preço total é R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é de %08X' %(1500, 1500))