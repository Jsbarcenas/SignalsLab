import numpy as np
from tkinter import *
from scipy import signal as sp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.filedialog import askopenfilename
import soundfile as sf
from tkinter import ttk
import os
import myStat as st


emgFile1, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_1.wav')
emgFile2, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_2.wav')
emgFile3, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_3.wav')
emgFile4, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_4.wav')
emgFile5, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_5.wav')
emgFile6, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_6.wav')
emgFile7, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_7.wav')
emgFile8, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_8.wav')
emgFile9, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_9.wav')
emgFile10, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/Fatigadas EMG/F_emg_10.wav')

lista = [emgFile1, emgFile2, emgFile3, emgFile4, emgFile5,
         emgFile6, emgFile7, emgFile8, emgFile9, emgFile10]

lista2 = [np.abs(np.fft.fft(emgFile1)), np.abs(np.fft.fft(emgFile2)), np.abs(np.fft.fft(emgFile3)), np.abs(np.fft.fft(emgFile4)), np.abs(np.fft.fft(
    emgFile5)), np.abs(np.fft.fft(emgFile6)), np.abs(np.fft.fft(emgFile7)), np.abs(np.fft.fft(emgFile8)), np.abs(np.fft.fft(emgFile9)), np.abs(np.fft.fft(emgFile10)), ]


met = [st.media, st.median, st.desviation, st.varianceABS, st.q1, st.q3, st.iqr,
       st.asymmetry, st.Kurtosis, st.CoeficienteVariacion, st.potency]
N = len(lista)

# for y in range(N):
#     s = 0
#     for x in lista:
#         s += met[y](x)
#         f = s/10
#         print(f)
s = 0
for x in lista:
    s += st.Kurtosis(x)

f = s/N
print(f)


# NO fatigada EMG

kmedia_N_EMG = 12.213226832737003
pmedia_N_EMG = 19.044327990740165


# Fatigadas EMG

pmedia_F_EMG = 27.279467078496953
kmedia_F_EMG = 6.7774214457958335
