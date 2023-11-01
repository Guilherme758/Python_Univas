contatos = [
            {'nome': 'Guilherme Henrique', 'telefone': '35984338501'},
            {'nome': 'João Pedro', 'telefone': '35911111111'},
            {'nome': 'Ana Clara', 'telefone': '35922222222'}
           ]

# Imprimindo todas as informações
cont = 1
for contato in contatos:
    print(f'Contato {cont}')
    print(f'''Nome: {contato['nome']}\nTelefone: {contato['telefone']}\n''')
    cont += 1

# Imprimindo o primeiro nome e o telefone
print(f'Imprimindo primeiro nome e telefone:\n{contatos[0]["nome"]}\n{contatos[0]["telefone"]}')