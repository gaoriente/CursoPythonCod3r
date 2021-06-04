import math  # Importa toda biblioteca
import sys


class TerminalColor:
    ERRO = '\033[91m'  # Cor vermelha
    NORMAL = '\033[0m'  # Volta a cor original


def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print("É necessário informar o raio do circulo.")
    print("Sintaxe: {} <raio>".format(sys.argv[1][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)  # encerra o programa
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO +
              "O raio deve ser um valor númerico" +
              TerminalColor.NORMAL)
        sys.exit(2)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Área do círculo', area)
