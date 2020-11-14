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
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_1.wav')
emgFile2, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_2.wav')
emgFile3, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_3.wav')
emgFile4, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_4.wav')
emgFile5, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_5.wav')
emgFile6, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_6.wav')
emgFile7, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_7.wav')
emgFile8, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_8.wav')
emgFile9, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_9.wav')
emgFile10, fs = sf.read(
    '/Users/Sjbarcx/Desktop/archivos señales/NO fatigadas EMG/N_emg_10.wav')

lista = [emgFile1, emgFile2, emgFile3, emgFile4, emgFile5,
         emgFile6, emgFile7, emgFile8, emgFile8, emgFile9, emgFile10]
Ppromedio = st.media(emgFile1)

met = [st.media, st.median, st.desviation, st.varianceABS, st.q1, st.q3, st.iqr,
       st.asymmetry, st.Kurtosis, st.CoeficienteVariacion, st.potency]
N = len(met)
s = 0
for y in range(N):
    for x in lista:
        s += met[y](x)
        f = s/10
        print(f)


# Fatigada EMG medias

mMedia_F_EMG = 0.014629121644715179
mDeviation_F_EMG = 0.17688753687688624
mMedian_F_EMG = 0.0068084716796875
mDesviationAbs_F_EMG = 0.10069689120482113
mQ1_F_EMG = -0.014935302734375
mQ2_F_EMG = 0.0499298095703125
mIqr_F_EMG = 0.0648651123046875
mAsymmetry_F_EMG = 0.18205619621742625
mKurtosis_F_EMG = 7.535426163237185
mCoeVar_F_EMG = 15.009309179742067
mPOtency_F_EMG = 0.014620087610619479


# NO fatigada  EMG Medias

mMedia_N_EMG = 0.014629121644715179
mDeviation_N_EMG = 0.17688753687688624
mMedian_N_EMG = 0.0068084716796875
mDesviationAbs_N_EMG = 0.10069689120482113
mQ1_N_EMG = -0.014935302734375
mQ2_N_EMG = 0.0499298095703125
mIqr_N_EMG = 0.0648651123046875
mAsymmetry_N_EMG = 0.18205619621742625
mKurtosis_N_EMG = 7.535426163237185
mCoeVar_N_EMG = 15.009309179742067
mPOtency_N_EMG = 0.014620087610619479
