import random
import numpy as np
import math
import matplotlib.pyplot as plt


def media_varianza(arr):
    print("La media è: ", np.mean(arr))
    print("La varianza è: ", np.var(arr))


def uniforme01(arrunifo, nbins):
    print("Uniforme")
    plt.hist(arrunifo, range=(0, max(arrUnifo)), bins=nbins)
    plt.title("Distribuzione uniforme tra 0, 1")
    plt.show()
    media_varianza(arrunifo)


def uniformeab(a, b, arrunifo, arrunifoab, nbins, listiniziale):
    for k in listiniziale:
        arrunifoab.append(k * (b - a) + a)
    print("Uniforme tra a e b")
    plt.hist(arrunifo, range=(0, max(arrunifo)), bins=nbins)
    plt.title("Distribuzione uniforme tra a e b")
    plt.show()
    media_varianza(arrunifo)


def esponenziale(arresp, listiniziale, nbins):
    for h in listiniziale:
        arresp.append((-1 / 0.3103) * math.log(1 - h, math.e))

    print("Esponenziale")
    plt.hist(arresp, range=(0, max(arresp)), bins=nbins)
    plt.title("Distribuzione esponenziale tra 0 ed 1")
    plt.show()
    media_varianza(arresp)


def lorentiana(arrlor, tau, listainiziale, nbins):
    for m in listainiziale:
        arrlor.append(tau * math.tan(math.pi * (m - 0.5)))

    print("Lorentiana")
    plt.hist(arrlor, range=(-10, 10), bins=nbins)
    plt.title("Distribuzione Lorentziana")
    plt.show()
    media_varianza(arrlor)


#  Genera gaussianna con metodo boxer ma solo unifoorme cioè tra 0,1 sono i numeri usciti
def gaussiana():
    h = np.random.uniform(size=1000)
    k = np.random.uniform(size=1000)
    r = np.sqrt(-2 * np.log(h))
    theta = 2 * np.pi * k
    x = r*np.sin(theta)
    print("Gaussiana")
    plt.hist(x)
    plt.title("Distribuzione Gaussiana")
    plt.show()
    media_varianza(x)



mylist = []
num = 10000
i = 0
f = 1
n = []
arrUnifo = []
arrUnifo2 = []
arrEsp = []
arrLor = []
nbins1 = 1000


for x in range(num):
    r = random.uniform(i, f)
    mylist.append(r)

for x in range(num):
    n.append(x + 1)

for item in mylist:
    arrUnifo.append(item * (f - i) + i)


uniforme01(arrUnifo, nbins1)

uniformeab(0, 30, arrUnifo, arrUnifo2, nbins1, mylist)

esponenziale(arrEsp, mylist, nbins1)

lorentiana(arrLor, 1, mylist, nbins1)

gaussiana()
