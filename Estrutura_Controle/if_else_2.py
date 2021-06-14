def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor idade'
    elif idade in range(18, 65):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        'Centenário'
    else:
        return 'Idade Inválida'


if __name__ == '__main__':
    idades = (17, 35, 87, 113, -2)
    # Se quiser mandar direto, sem armazenar em uma variavel, é só tirar idades e por os valores
    # for idade in (17, 35, 87, 113, -2):
    for idade in idades:
        print(f'{idade}: {faixa_etaria(idade)}')
