# Callable

def executar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom dia! Callable executado')


def bom_tarde():
    print('Bom tarde! Callable executado')


if __name__ == '__main__':
    executar(bom_dia)
    executar(bom_tarde)
    executar(1)
