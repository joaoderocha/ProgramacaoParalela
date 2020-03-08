import numpy


def vezes(a, b):
    return a * b


def multLinhaPorCol(vetor1, vetor2):
    tamanho = len(vetor1)
    return sum([vezes(vetor1[i], vetor2[i]) for i in range(tamanho)])


def geradorMatriz(tamanho):
    with open("matriz.txt", "w") as f:
        for linha, i in [(numpy.random.rand(tamanho, ), i) for i in range(tamanho)]:
            f.writelines(('{}' + str(linha) + '\n').format(i))
        return f.name
