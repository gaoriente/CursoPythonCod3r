for x in range(1, 11):
    if x % 2 == 0:
        continue  # continue interrompe a iteração e vai para próxima iteração, com isso imprime os impares
    print(x)

for x in range(1, 11):
    if x == 5:
        break  # interrompe o laço quando der boa a condição
    print(x)

print('Fim!')
