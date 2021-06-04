import math  # Importa toda biblioteca


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area = circulo(raio)
    print('Área do círculo', area)
