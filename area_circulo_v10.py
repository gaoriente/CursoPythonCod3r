import math  # Importa toda biblioteca
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[1][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)  # encerra o programa
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)
