#!/usr/local/bin/python3

arquivo = open('pessoas.csv')
for registro in arquivo:
    # Strip remove os espaços
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
