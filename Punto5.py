import random
import numpy as np
import math
import matplotlib.pyplot as plt


def media_varianza(arr):
    print("La media è: ", np.mean(arr))
    print("La varianza è: ", np.var(arr))
    print("La deviazione standard è: ", np.std(arr))
    print("")


def mediacomando(arr, passo):
    inizio = 0
    fine = passo
    media = []
    for item in arr[::passo]:
        media.append(np.mean(arr[inizio:fine]))
        inizio = inizio + passo
        fine = fine + passo
    print("La media della media è:", np.mean(media))
    print("La sigma (stdev) della media è:", np.std(media))
    print("")
    print("")
    return media


def mediecomandi(arr, tipdist):
    media5 = mediacomando(arr, 5)
    plt.hist(media5, range=(min(media5), max(media5)), color='#FFFD98')
    plt.title(tipdist + " distribuzione delle medie ogni 5")
    plt.savefig(tipdist + " distribuzione delle medie ogni 5")
    plt.show()
    media10 = mediacomando(arr, 10)
    plt.hist(media10, range=(min(media10), max(media5)), color='#BDE4A7')
    plt.title(tipdist + " distribuzione delle medie ogni 10")
    plt.savefig(tipdist + " distribuzione delle medie ogni 10")
    plt.show()
    media50 = mediacomando(arr, 50)
    plt.hist(media50, range=(min(media50), max(media5)), color='#B3D2B2')
    plt.title(tipdist + " distribuzione delle medie ogni 50")
    plt.savefig(tipdist + " distribuzione delle medie ogni 50")
    plt.show()
    media100 = mediacomando(arr, 100)
    plt.hist(media100, range=(min(media100), max(media5)), color='#9FBBCC')
    plt.title(tipdist + " distribuzione delle medie ogni 100")
    plt.savefig(tipdist + " distribuzione delle medie ogni 100")
    plt.show()


def uniforme01(arrunifo, nbins):
    print("Uniforme")
    plt.hist(arrunifo, range=(0, max(arrUnifo)), bins=nbins, color='#BCC4DB')
    plt.title("Distribuzione uniforme tra 0, 1")
    plt.savefig("x Distribuzione uniforme 01.png")
    plt.show()
    media_varianza(arrunifo)
    mediecomandi(arrunifo, "uniforme")
    print("")
    print("")
    print("")
    print("")


def uniformeab(a, b, arrunifo, arrunifoab, nbins, listiniziale):
    for k in listiniziale:
        arrunifoab.append(k * (b - a) + a)
    print("Uniforme tra a e b")
    plt.hist(arrunifo, range=(0, max(arrunifo)), bins=nbins)
    plt.title("Distribuzione uniforme tra a e b")
    plt.savefig("x Distribuzione uniforme ab.png")
    plt.show()
    media_varianza(arrunifoab)


def esponenziale(arresp, listiniziale, nbins):
    for h in listiniziale:
        arresp.append((-1 / 0.3103) * math.log(1 - h, math.e))

    print("Esponenziale")
    plt.hist(arresp, range=(0, max(arresp)), bins=nbins, color='#C0A9B0')
    plt.title("Distribuzione esponenziale tra 0 ed 1")
    plt.savefig("x Distribuzione esponenziale 01.png")
    plt.show()
    media_varianza(arresp)
    mediecomandi(arresp, "Esponenziale")
    print("")
    print("")
    print("")
    print("")


def lorentiana(arrlor, tau, listainiziale, nbins):
    for m in listainiziale:
        arrlor.append(tau * math.tan(math.pi * (m - 0.5)))

    print("Lorentiana")
    plt.hist(arrlor, range=(-10, 10), bins=nbins, color='#7880B5')
    plt.title("Distribuzione Lorentziana")
    plt.savefig("x Distribuzione Lorentiana.png")
    plt.show()
    media_varianza(arrlor)
    print("")
    print("")
    print("")
    print("")


#  Genera gaussianna con metodo boxer ma solo unifoorme cioè tra 0,1 sono i numeri usciti
def gaussiana(siz):
    h = np.random.uniform(size=siz)
    k = np.random.uniform(size=siz)
    r = np.sqrt(-2 * np.log(h))
    theta = 2 * np.pi * k
    x = r*np.sin(theta)
    print("Gaussiana")
    plt.hist(x, color='#6987C9')
    plt.title("Distribuzione Gaussiana")
    plt.savefig("x Distribuzione Gaussiana.png")
    plt.show()
    media_varianza(x)
    mediecomandi(x, "Gaussiana")
    print("")
    print("")
    print("")
    print("")


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


print("Il numero di eventi generati è:", num, "con un bin di:", nbins1)
print("")
print("")
print("")
print("")

for x in range(num):
    r = random.uniform(i, f)
    mylist.append(r)

for x in range(num):
    n.append(x + 1)

for item in mylist:
    arrUnifo.append(item * (f - i) + i)


uniforme01(arrUnifo, nbins1)

#  uniformeab(0, 30, arrUnifo, arrUnifo2, nbins1, mylist)

esponenziale(arrEsp, mylist, nbins1)

lorentiana(arrLor, 1, mylist, nbins1)

gaussiana(num)
