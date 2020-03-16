import concurrent.futures
import time

import matplotlib.pylab as plt
import numpy

from helpers import verificaResultado, multLinhaPorCol, guardaResultado, geraTabela

verifica = True


def runThreading(numeroThreads, matriz, vetorOp, ):
    vetor = []
    t1 = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=numeroThreads) as executor:
        for linha in matriz:
            vetor.append(executor.submit(multLinhaPorCol, linha, vetorOp))
    tempoThreads = time.time() - t1

    tempoSequencial = 0
    if verifica:
        t1 = time.time()
        verificaResultado(matriz, vetorOp, vetor)
        tempoSequencial = time.time() - t1
    return tempoThreads, tempoSequencial


if __name__ == '__main__':
    resultados = dict()
    numeroInstancias = 4
    valorInicialInstancias = 1
    numeroMaximoTheads = 10
    numeroStepsEmThreads = 2
    valorInicialThreads = 2
    numeroResultados = numeroInstancias * round(numeroMaximoTheads / numeroStepsEmThreads)
    axes = plt.gca()
    axes.set_xlim([pow(10, valorInicialInstancias), pow(10, numeroInstancias)])
    plt.xlabel('instancias')
    plt.ylabel('tempo')
    print('---------- Running Test Suit -------------')
    for tamanhoInstancia in range(valorInicialInstancias, numeroInstancias):
        x = y = pow(10, tamanhoInstancia)
        for numeroThreads in range(valorInicialThreads, numeroMaximoTheads, numeroStepsEmThreads):
            matrizCompartilhada = numpy.random.randint(1, 100, size=(x, y))
            vetorMultiplicacao = numpy.random.randint(1, 100, size=x)
            result = runThreading(numeroThreads, matrizCompartilhada, vetorMultiplicacao)
            guardaResultado(x, numeroThreads, (round(result[0], 4), round(result[0], 4)), resultados)

    df1, df2 = geraTabela(resultados)
    print('Paralelo:\n', df1, '\n', 'Sequencial:\n', df2)
