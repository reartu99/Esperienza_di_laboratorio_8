import random
import numpy as np
import math
import matplotlib.pyplot as plt


# Questa funzione ritorna media e variaza su una list di valori
def media_varianza(arr):
    print("La media è: ", np.mean(arr))
    print("La varianza è: ", np.var(arr))


#  Questa funzione genera n numeri uniformi tra un massimo ed un minimo, ritorna una list
def genera_numeri(minimum, maximum, eventi):
    mylist = []
    for x in range(eventi):
        r = random.uniform(minimum, maximum)
        mylist.append(r)
    return mylist


#  Questa funzione salva un grafico distribuzione uniforme e ritorna i parametri dell'hist
def distribuzione_uniforme(lista, minimum, maximum, passo):
    a, b, c = plt.hist(lista, bins=np.arange(minimum, maximum + passo, passo))
    plt.title("Distribuzione uniforme")
    plt.savefig("Distribuzione uniforme.png")
    plt.show()

    return a, b, c


def poisson(lista):
    a, b, c = plt.hist(lista, bins=int((lista.max()-lista.min())))
    plt.title("Poissoniana valori ottenuti")
    plt.savefig("Poissoniana ottenuta.png")
    plt.show()
    partenza = lista.min()
    arrivo = lista.max()

    return a, b, partenza, arrivo


def poisson_attesa(nprov, nbinor, orarr):
    mu = nprov/nbinor
    pmf = []
    #  nbinor è il numero di bin originale, nprov sono gli eventi
    #  orarr è l'array originale

    for item in orarr:
        pmfi = np.exp(-mu)*(mu**item)/math.factorial(int(item))
        pmf.append(pmfi*nbinor)

    plt.bar(orarr, pmf, label='osservato')
    plt.title("Poissoniana valori attesi")
    plt.savefig("Poissoniana attesa.png")
    plt.show()

    return pmf


def poissonconfronto(a, pmf, range1, range2):
    plt.bar(range1, a)
    plt.bar(range2, pmf, alpha=0.4)
    plt.show()


events = 10000  # Numero di eventi generati
nbins = 200   # Numero di bins
minimo = 0
massimo = 10
Dx = massimo/nbins

print("Il numero di eventi é: ", events)
print("Il numero di bins é: ", nbins)
print("Gli eventi generati vanno da ", minimo, " a ", massimo)
print("Il passo è quindi dato da massimo/numero di bin cioè: ", Dx)
print("")
print("")

slist = genera_numeri(minimo, massimo, events)

aarray, barray, carray = distribuzione_uniforme(slist, minimo, massimo, Dx)
print("La media e la varianza della uniforme")
media_varianza(slist)
print("")

array1, bins1, partenza1, arrivo1 = poisson(aarray)
print("La media e la varianza della poisson ottenuta")
media_varianza(aarray)
print("")

pmf1 = poisson_attesa(events, nbins, bins1)
print("La media e la varianza della poisson attesa")
media_varianza(bins1)
print("")


ranges1 = np.arange(partenza1, arrivo1, 1)
poissonconfronto(array1, pmf1, ranges1, bins1)
