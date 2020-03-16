import pandas as pd


def verificaResultado(matrizOriginal, vetorMult, vetorResultante):
    partial = []
    for i in range(len(matrizOriginal)):
        for j in range(len(vetorMult)):
            partial.append(matrizOriginal[i][j] * vetorMult[j])

        if sum(partial) != vetorResultante[i].result():
            print("errou")
            return
        partial.clear()


def guardaResultado(tamanhoInstancia, numeroThreads, resultados, dicionario):
    subDict1 = {
        'tamanhoInstancia': tamanhoInstancia,
        'numeroThreads': numeroThreads,
        'tempo': resultados[0]
    }
    subDict2 = {
        'tamanhoInstancia': tamanhoInstancia,
        'numeroThreads': numeroThreads,
        'tempo': resultados[1]
    }
    valor = len(dicionario)
    key = 'paralelo {}'.format(valor + 1)
    dicionario.update({key: subDict1})
    key = 'sequencial {}'.format(valor + 2)
    dicionario.update({key: subDict2})


def geraTabela(resultados):
    paralelos = []
    sequenciais = []

    for key, value in resultados.items():
        if key.startswith('paralelo'):
            paralelos.append(value)
        if key.startswith('sequencial'):
            sequenciais.append(value)

    paraleloPlot = {}
    for k in paralelos[0].keys():
        paraleloPlot[k] = tuple(paraleloPlot[k] for paraleloPlot in paralelos)

    sequencialPlot = {}
    for k in sequenciais[0].keys():
        sequencialPlot[k] = tuple(sequencialPlot[k] for sequencialPlot in sequenciais)

    dfP = pd.DataFrame(index=(set(paraleloPlot['tamanhoInstancia'])),
                       columns=(set(paraleloPlot['numeroThreads'])))

    dfS = pd.DataFrame(index=(set(sequencialPlot['tamanhoInstancia'])),
                       columns=(set(sequencialPlot['numeroThreads'])))

    tempos = paraleloPlot['tempo']
    temposS = sequencialPlot['tempo']
    instancia = paraleloPlot['tamanhoInstancia']
    nThreads = paraleloPlot['numeroThreads']
    for i in range(len(tempos)):
        dfP.at[instancia[i], nThreads[i]] = '{} ms'.format(tempos[i])
        dfS.at[instancia[i], nThreads[i]] = '{} ms'.format(temposS[i])

    return dfP.sort_index().sort_index(1), dfS.sort_index().sort_index(1)
