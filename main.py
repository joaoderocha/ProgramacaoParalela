import numpy
import concurrent.futures
import time
from helpers import verificaResultado, multLinhaPorCol

tamanhoVetores = x = y = 10000
numeroWorkers = 8
verifica = True

matrizCompartilhada = numpy.random.rand(x, y)
vetorMultiplicacao = numpy.random.rand(x, )


def runThreading():
    vetor = []
    t1 = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=numeroWorkers) as executor:
        for linha in matrizCompartilhada:
            vetor.append(executor.submit(multLinhaPorCol, linha, vetorMultiplicacao))
    t2 = time.clock() - t1

    print("runtime(ms) paralelo com threads:", t2)

    if verifica:
        try:
            t1 = time.clock()
            verificaResultado(matrizCompartilhada, vetorMultiplicacao, vetor)
            t2 = time.clock() - t1
            print("runtime(ms) sequencial:",t2)
        except AssertionError:
            print("errou")


if __name__ == '__main__':
    print("Execucao com threads")
    runThreading()

