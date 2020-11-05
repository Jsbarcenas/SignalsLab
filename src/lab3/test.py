from math import sqrt
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import kurtosis
from scipy.stats import skew
import statistics as sta
from scipy import ndimage
# // Kurtosis


def Kurtosis(lista):
    n = mean = M2 = M3 = M4 = 0

    for x in lista:
        n1 = n
        n = n + 1
        delta = x - mean
        delta_n = delta / n
        delta_n2 = delta_n * delta_n
        term1 = delta * delta_n * n1
        mean = mean + delta_n
        M4 = M4 + term1 * delta_n2 * \
            (n*n - 3*n + 3) + 6 * delta_n2 * M2 - 4 * delta_n * M3
        M3 = M3 + term1 * delta_n * (n - 2) - 3 * delta_n * M2
        M2 = M2 + term1

    kurtosis = (n*M4) / (M2*M2) - 3
    return kurtosis


# media


def media(lista):
    s = 0
    for element in lista:
        s += element
    return s / float(len(lista))

# variazan


def variance(lista):
    s = 0
    m = media(lista)
    for element in lista:
        s += (element - m) ** 2
    return s / float(len(lista))

# variance absoluta


def varianceABS(lista):
    s = 0
    m = media(lista)
    for element in lista:
        s += abs((element - m))
    return s / float(len(lista))

# Desviación estandar


def desviation(lista):
    return sqrt(variance(lista))


lis = [1, 2, 6, 10, 5, 88]


# Mediana


def median(l):
    half = len(l) // 2
    l.sort()
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]


# Asimetría

def varianceN(lista):
    s = 0
    m = media(lista)
    for element in lista:
        s += (element - m) ** 3
    return s / float(len(lista))


def asymmetry(lista):
    return varianceN(lista)/desviation(lista)**3


# Coeficiente de variación

def CoeficienteVariacion(lista):
    return desviation(lista)/media(lista)


# potency
def potency(lista):
    n = float(len(lista))
    s = 0
    m = media(lista)
    for element in lista:
        s += (element)**2
    return s*(1/(2*n+1))


print(asymmetry(lis))


def q2(lista):
    orderData = sorted(lis)
    if not len(lista) % 2:
        q = 2*(float(len(lista))) / 4
    q = 2*(float(len(lista))+1)/4
    return q


print(median(lis))
print(q2(lis))
