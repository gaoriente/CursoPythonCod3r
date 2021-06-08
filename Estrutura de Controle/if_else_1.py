# Conceitos     Notas
# A             De 10,0 a 9,1
# A-            De 9 a 8,1
# B             De 8 a 7,1
# B-            De 7 a 6,1
# C             De 6 a 5,1
# C-            De 5 a 4,1
# D             De 4 a 3,1
# D-            De 3 a 2,1
# E             De 2 a 1,1
# E-            De 1 a 0
#
#  * Para Notas maiores que 10 e menores que 0 será impresso "nota inválida"

def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        print("Nota inválida!")
    elif nota >= 9.1:
        print("A")
    elif nota >= 8.1:
        print("A-")
    elif nota >= 7.1:
        print("B")
    elif nota >= 6.1:
        print("B-")
    elif nota >= 5.1:
        print("C")
    elif nota >= 4.1:
        print("C-")
    elif nota >= 3.1:
        print("D")
    elif nota >= 2.1:
        print("D-")
    elif nota >= 1.1:
        print("E")
    elif nota >= 0:
        print("E-")
    elif nota < 0:
        print("Nota inválida")


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
