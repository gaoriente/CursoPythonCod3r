#!/usr/local/bin/python3

try:
    arquivo = open('pessoas.csv')
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
finally:  # Mesmo que der erro no try, o finally ocorre
    print('finally')
    arquivo.close()

if arquivo.closed:
    print('Arquivo fechado!')
