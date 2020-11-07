from math import sqrt
import matplotlib.pyplot as plt
import scipy.stats as stats
import statistics as st
import scipy.stats as ss
import statistics as sta
from scipy.stats import kurtosis as k
import math
import numpy as np

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
    return s / (float(len(lista))-1)

# variance absoluta


def varianceABS(lista):
    s = 0
    m = media(lista)
    for element in lista:
        s += np.abs(element - m)
    return s / float(len(lista)-1)

# Desviación estandar


def desviation(lista):
    return sqrt(variance(lista))


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
    return s / float(len(lista)-1)


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
        s += np.abs((element)**2)
    return s*(1/(2*n+1))


# Quartil 1


def q1(lista):
    Orderlist = sorted(lista)
    return Orderlist[int(len(Orderlist)/4)-1]


# Quartil 2

def q3(lista):
    Orderlist = sorted(lista)
    return Orderlist[int((3*len(Orderlist))/4)-1]


# IQR


def iqr(lista):
    iqr = q3(lista)-q1(lista)
    return iqr


###########################################################


lis = [6, 8, 3, 2, 6, 5, 6, 4, 5, 5, 2, 5, 6, 4, 2]


def Media2(lista):
    suma = 0
    N = len(lista)
    for data in lista:
        suma = suma + data
    return (1/N)*suma


def Mediana2(lista):
    orderList = sorted(lista)
    N = len(lista)
    pos = int((N+1)/2)
    return orderList[pos]


def desviation2(lista):
    N = len(lista)
    x = 0
    for data in lista:
        x = x+(data-Media2(lista))**2
    return ((1/N)*x)**1/2
