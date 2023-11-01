lst_nomes = ['ana', 'pedro', 'joão', 'lucas', 'maria', 'guilherme', 'mateus', 'eduardo', 'davi', 'luiza']

# 3 primeiros nomes
print(f'3 primeiros nomes: {lst_nomes[:3]}')

# Nomes em ordem alfabética
lst_nomes.sort()

print(f'Nomes em ordem alfabética: {lst_nomes}')

# Nomes em maiúsculo
print(f'Nomes em maiúsculo: {[nome.upper() for nome in lst_nomes]}')

