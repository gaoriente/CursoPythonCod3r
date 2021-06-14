palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=",")  # o end faz quebrar o padrão de saida final.
print('Fim')

aprovados = ['Gabriel', 'Gabriela', 'Eduardo', 'Crews']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    # print(posicao + 1, nome)
    print(f'{posicao + 1})', nome)

dias_semana = ('Domingo', 'Segunda', 'Terça',
               'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')

for letra in set('muito legal'):
    print(letra)
