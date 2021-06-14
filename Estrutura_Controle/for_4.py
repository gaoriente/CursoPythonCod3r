# for i in range(1, 11):
#    if i == 6:
#        break
#    print(i)
# else:
#    print('Fim!')

# funcao sortear_dado -> sorteia numeros entre 1 e 6
# for com range 1 a 6 (incluindo 6)
# se o numero for impar continue
# se o numero for par e for igual ao valor sorteado pela funcao dado, imprimir `Acertou`
# e depois chamar o break
# se nao acertar chama o else... print('Nao acertou')

from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortear_dado() == i:
        print('Acertou', i)
        break
else:
    print('ERROU')
