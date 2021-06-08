# Percorrendo dicionario

produto = {'Nome': 'Caneta Chic', 'Preço': 14.99,
           'importado': True, 'estoque': 793}

# for chave in produto.key() Redundante mas funciona
for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
