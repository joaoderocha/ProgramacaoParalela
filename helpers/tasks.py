def vezes(a, b):
    return a * b


def multLinhaPorCol(vetor1, vetor2):
    tamanho = len(vetor1)
    return sum([vezes(vetor1[i], vetor2[i]) for i in range(tamanho)])
