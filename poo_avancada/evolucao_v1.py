class Humano:
    # atributo de classe
    especie = 'Homo sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Aistralopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especie()[-2]


class HomoSapiens(Humano):
    especie = Humano.especie()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')
    print(f'Evolução (a partir da classe): {",".join(HomoSapiens.especie())}')
    print(f'Evolução (a partir da classe): {",".join(jose.especie())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neanderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {grokn.is_evoluido()}')
