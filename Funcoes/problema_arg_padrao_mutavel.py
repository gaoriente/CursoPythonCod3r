def fibonacci(sequencia=[0, 1]):
    # uso de mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

    # para dar certo, tem que transformar em uma tupla, então o código ficaria assim
    # def fibonacci(sequencia=(0, 1)):
    # #uso de mutáveis como valor default (armadilha)
    # return sequencia + (sequencia[-1] + sequencia[-2],)
    #
    #


if __name__ == '__main__':
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci()
    print(restart, id(restart))
    # assert restart == [0, 1, 1]
