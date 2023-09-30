# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso, a expressao inteira avaliada naquele valor
# São considerados falsy: 0 0.0 . ' ' False
# Também existe o tipo None usado para representar um não-valor

entrada = input('[E]ntrar [S]sair:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')


# Avaliacao de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
