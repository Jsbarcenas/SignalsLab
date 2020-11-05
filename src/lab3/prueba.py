from math import sqrt
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import kurtosis
import numpy as np
from scipy.stats import skew

lista = [1, 2, 3, 1, 4, 56, 8, 5, 4, 63, 65]


def media(data):
    s = 0
    for elemento in lista:
        s += elemento
    return s / float(len(lista))

# variazan


def varianza(data):
    s = 0
    m = media(lista)
    for elemento in lista:
        s += (elemento - m) ** 2
    return s / float(len(lista))

    # Desviación estandar


def desviacion_tipica(lista):
    return sqrt(varianza(lista))


def varianzaN(lista):
    s = 0
    m = media(lista)
    for elemento in lista:
        s += (elemento - m) ** 3
    return s / float(len(lista))


def Asimetria(lista):
    return varianzaN(lista)/desviacion_tipica(lista)**3


print(Asimetria(lista))
print(skew(lista))
