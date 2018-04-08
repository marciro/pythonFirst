def mostra_nome_na_tela(nome):
    print(nome)
    return

def nome_completo_usuario(codigo):
    print('Marcelo Cicero Rodrigues da Costa')
    return 'Marcelo Cicero', 'Rodrigues da Costa'

mostra_nome_na_tela('Teste')
nome,sobrenome = nome_completo_usuario(1)
print(nome+' '+sobrenome)