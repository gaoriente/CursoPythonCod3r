def fibonacci(quantidade):
    resultado = [0, 1]

    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == quantidade:  # Condiçao de parada o tamanho do array
            break
    return resultado


if __name__ == '__main__':
    # listar os 20 primeiros números da sequência
    for fib in fibonacci(20):
        print(fib)
