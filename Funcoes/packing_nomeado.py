# **kwargs
def resultado_f1(**podium): # Quando eu uso 2 * = o parâmetro é nomeado
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}' )


if __name__ == '__main__':
    resultado_f1(primeiro = 'L. Hamilton',
                segundo = 'M. Verstappen',
                terceiro = 'S. Vettel')