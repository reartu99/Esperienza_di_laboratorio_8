import random
import numpy as np
import math
import matplotlib.pyplot as plt
import decimal


decimal.getcontext().prec = 10000000000

# Questa funzione ritorna media e variaza su una list di valori


def media_varianza(arr):
    med = 0
    devianza = 0

    for item in arr:  # Questa riga fa la media aritmetica
        med = float(med) + float(item)
    med = med / len(arr)
    print("La media è: ", med)

    for item in arr:
        devianza = devianza + ((item - med) ** 2)

    varianza = np.sqrt(devianza / len(arr))
    print("La varianza è: ", varianza)
    return med, varianza


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
    a, b, c = plt.hist(lista, bins = int((lista.max()-lista.min()))) #  , bins=np.arange(minimum, len(set(lista)) + 1))
    plt.title("Poissoniana valori ottenuti")
    plt.savefig("Poissoniana ottenuta.png")
    plt.show()

    return a, b, c


def poisson_attesa(nprov, nbinor, orarr):
    mu = nprov/nbinor
    pmf = []

    for item in orarr:
        pmfi = np.exp(-mu)*(mu**item)/math.factorial(int(item))
        pmf.append(pmfi*nbinor)

    plt.bar(orarr, pmf, label = 'osservato')
    plt.title("Poissoniana valori attesi")
    plt.savefig("Poissoniana attesa.png")
    plt.show()

#  Prova

def poissonconfronto(a, b, newlen):
    plt.hist([a, b], bins=np.arange(0, newlen + 1), label=["Osservata", "Attesa"])
    plt.title("Distribuzioni attese e ottenute a confronto")
    plt.savefig("Distribuzioni attese e ottenute a confronto.png")
    plt.legend(prop={'size': 10})
    plt.show()


events = 10000  # Numero di eventi generati
nbins = 200   # Numero di bins
minimo = 0
massimo = 10
Dx = massimo/nbins

slist = genera_numeri(minimo, massimo, events)

aarray, barray, carray = distribuzione_uniforme(slist, minimo, massimo, Dx)
print("La media e la varianza della uniforme")
media_varianza(slist)

array1, barray1, carray1 = poisson(aarray)
print("La media e la varianza della poisson ottenuta")
media_varianza(aarray)

poisson_attesa(events, nbins, barray1)
print("La media e la varianza della poisson attesa")
media_varianza(array1)

#  poissonconfronto(aarray, array2, newlen2)
