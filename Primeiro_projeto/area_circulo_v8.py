import math  # Importa toda biblioteca
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio)
    print('Área do círculo', area)
