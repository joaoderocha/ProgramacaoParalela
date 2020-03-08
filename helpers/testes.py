def verificaResultado(matrizOriginal, vetorMult, vetorResultante):
    partial = []
    for i in range(len(matrizOriginal)):
        for j in range(len(vetorMult)):
            partial.append(matrizOriginal[i][j] * vetorMult[j])
        if sum(partial) != vetorResultante[i].result():
            raise AssertionError
        partial.clear()