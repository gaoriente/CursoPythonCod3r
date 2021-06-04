import math  # Importa toda biblioteca


def circulo(raio):
    print('Área do círculo', math.pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('Informe o raio: ')
    circulo(raio)
