# Today October 23 at 11:30 pm, I start to program this code.
# I hope you like reading it. You have many optimizations and descriptions
# evolved with respect to previous deliveries. Well my way degenerate before
# functions was not very optimal. It was time to spend a whole day investigating in a simpler way
# Among colleagues and forums, I found a better description for all.
# Enjoy ;)


import numpy as np
from tkinter import *
from scipy import signal as sp
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk

main = Tk()
main.title('Fourier Series Homework')
main.configure(background='gainsboro', padx=30, pady=10)
main.geometry('400x400')
main.resizable(0, 0)

timeInitFuncEntry = Entry(main)
timeInitFuncEntry.configure(background='white')
timeInitFuncEntry.config(width=10)
timeInitFuncEntry.place(y=20, x=120)

timeInitFuncLab = Label(main, text="Time Init")
timeInitFuncLab .configure(background='white')
timeInitFuncLab .config(width=10)
timeInitFuncLab.place(y=20, x=20)

timeFinalFuncEntry = Entry(main)
timeFinalFuncEntry.configure(background='white')
timeFinalFuncEntry.config(width=10)
timeFinalFuncEntry.place(y=60, x=120)

timeFinalFuncLab = Label(main, text="Time Final")
timeFinalFuncLab.configure(background='white')
timeFinalFuncLab.config(width=10)
timeFinalFuncLab.place(y=60, x=20)

amplitudFuncEntry = Entry(main)
amplitudFuncEntry.configure(background='white')
amplitudFuncEntry.config(width=10)
amplitudFuncEntry.place(y=100, x=120)

amplitudFuncLab = Label(main, text="Amplitud")
amplitudFuncLab.configure(background='white')
amplitudFuncLab.config(width=10)
amplitudFuncLab.place(y=100, x=20)

tFuncEntry = Entry(main)
tFuncEntry.configure(background='white')
tFuncEntry.config(width=10)
tFuncEntry.place(y=140, x=120)

tFunLab = Label(main, text="T Value")
tFunLab.configure(background='white')
tFunLab.config(width=10)
tFunLab.place(y=140, x=20)

nFuncEntry = Entry(main)
nFuncEntry.configure(background='white')
nFuncEntry.config(width=10)
nFuncEntry.place(y=180, x=120)

nFuncLab = Label(main, text="N Value")
nFuncLab.configure(background='white')
nFuncLab.config(width=10)
nFuncLab.place(y=180, x=20)


def Action():
    ShowGraph()
    GrpahFourrierSeries()


def ShowGraph():
    global timeFuncGenerator
    global funcGenerator
    global nameFunc
    global tcarry
    global funcCarry
    timeInitGenerator = float(timeInitFuncEntry.get())
    timeFinalGenerator = float(timeFinalFuncEntry.get())
    a = float(amplitudFuncEntry.get())
    selectedFunc = functionSelectionEntry.get()
    timeStep = 0.01
    timeStimateFunc = 10/3
    timedelimitedStatus = 10
    if selectedFunc == "Signal_1":
        tInit = np.arange(0, 3, timeStep)
        tMediun = np.arange(3, 6, timeStep)
        tFin = np.arange(6, 9, timeStep)
        funInit = np.zeros(len(tInit))
        funMediun = np.exp(tMediun-3)-1
        funFinal = np.zeros(len(tFin))+funMediun[len(funMediun)-1]
        timeFuncGenerator = np.concatenate((tInit, tMediun, tFin), axis=None)
        funcGenerator = a * \
            np.concatenate((funInit, funMediun, funFinal), axis=None)
        tt = timeFuncGenerator/9 * \
            (timeFinalGenerator-timeInitGenerator)+timeInitGenerator
        nameFunc = 'Signal_1'
    if selectedFunc == "Signal_2":
        tInit = np.arange(0, timeStimateFunc, timeStep)
        tMediun = np.arange(timeStimateFunc, 2*timeStimateFunc, timeStep)
        tFin = np.arange(2*timeStimateFunc, timedelimitedStatus, timeStep)
        funInit = np.zeros(len(tInit))+timeStimateFunc
        funMediun = -(tMediun-timeStimateFunc*2)
        funFinal = np.zeros(len(tFin))
        timeFuncGenerator = np.concatenate((tInit, tMediun, tFin), axis=None)
        funcGenerator = a * \
            np.concatenate((funInit, funMediun, funFinal), axis=None)
        tt = timeFuncGenerator/timedelimitedStatus * \
            (timeFinalGenerator-timeInitGenerator)+timeInitGenerator
        nameFunc = 'Signal_2'
    if selectedFunc == "Signal_3":
        tInit = np.arange(0, timeStimateFunc, timeStep)
        tMediun = np.arange(timeStimateFunc, 2*timeStimateFunc, timeStep)
        tFin = np.arange(2*timeStimateFunc, timedelimitedStatus, timeStep)
        funInit = tInit
        funMediun = np.zeros(len(tMediun))+timeStimateFunc
        funFinal = -(tFin-timedelimitedStatus)
        timeFuncGenerator = np.concatenate((tInit, tMediun, tFin), axis=None)
        funcGenerator = a * \
            np.concatenate((funInit, funMediun, funFinal), axis=None)
        tt = timeFuncGenerator/timedelimitedStatus * \
            (timeFinalGenerator-timeInitGenerator)+timeInitGenerator
        nameFunc = 'Signal_3'
    if selectedFunc == "Signal_4":
        tInit = np.arange(0, timeStimateFunc, timeStep)
        tMediun = np.arange(timeStimateFunc, 2*timeStimateFunc, timeStep)
        tFin = np.arange(2*timeStimateFunc, timedelimitedStatus, timeStep)
        funInit = (np.exp(-tInit)-1)*(-1)
        funMediun = (np.exp(-tInit)-1)+max(funInit)
        funFinal = (np.exp(-tInit)-1)*(-1)
        timeFuncGenerator = np.concatenate((tInit, tMediun, tFin), axis=None)
        funcGenerator = a * \
            np.concatenate((funInit, funMediun, funFinal), axis=None)
        tt = timeFuncGenerator/timedelimitedStatus * \
            (timeFinalGenerator-timeInitGenerator)+timeInitGenerator
        nameFunc = 'Signal_4'
    if selectedFunc == "Signal_5":
        tInit = np.arange(0, timeStimateFunc, timeStep)
        tMediun = np.arange(timeStimateFunc, 2*timeStimateFunc, timeStep)
        tFin = np.arange(2*timeStimateFunc, timedelimitedStatus, timeStep)
        funInit = (np.exp(tInit)-1)*(-1)
        funMediun = (np.exp(tInit)-1)+min(funInit)
        funFinal = (np.exp(tInit)-1)*(-1)
        timeFuncGenerator = np.concatenate((tInit, tMediun, tFin), axis=None)
        funcGenerator = a * \
            np.concatenate((funInit, funMediun, funFinal), axis=None)
        tt = timeFuncGenerator/timedelimitedStatus * \
            (timeFinalGenerator-timeInitGenerator)+timeInitGenerator
        nameFunc = 'Signal_5'

    tcarry = tt
    funcCarry = funcGenerator


functionSelectionEntry = ttk.Combobox(main, values=[
                                      'Signal_1', 'Signal_2', 'Signal_3', 'Signal_4', 'Signal_5'], state="readonly")
functionSelectionEntry.place(y=220, x=20)
functionSelectionEntry.bind("<<ComboboxSelected>>", ShowGraph)

# This is where I complain about not having expected the second class of
# lab, I could have saved myself replicating the mathlab logic, for the
# representations of fourier ... well, happens. :D


def GrpahFourrierSeries():
    global timeFuncGenerator
    global funcGenerator
    timeStep = 0.01
    funcGenerator = funcGenerator
    TFuncStatus = float(tFuncEntry.get())
# Here i took all class code.
    T = timeFuncGenerator[len(timeFuncGenerator)-1]+timeStep
    Wo = 2*np.pi/T
    n = int(nFuncEntry.get())
    Ak = np.zeros((n, 1))
    Bk = np.zeros((n, 1))
    m = len(timeFuncGenerator)
    Nk = np.arange(1, n+1)
    Ck = np.zeros((n, 1))
    Phi_k = np.zeros((n, 1))
    A0 = 0
    for i in range(1, m):
        A0 = A0 + (1/T)*funcGenerator[i]*timeStep

    for i in range(1, n):
        for j in range(1, m):
            Ak[i] = Ak[i] + ((2/T)*funcGenerator[j] *
                             np.cos(i*timeFuncGenerator[j]*Wo))*timeStep
            Bk[i] = Bk[i] + ((2/T)*funcGenerator[j] *
                             np.sin(i*timeFuncGenerator[j]*Wo))*timeStep
        Ck[i] = ((Ak[i])**2 + (Bk[i])**2)**0.5
        Phi_k[i] = abs(-1*np.arctan(Bk[i]/Ak[i]))
    timeReconstructionGenerator = np.arange(0, 2*T, timeStep)
    funcReconstructionGenerator = 0
    for i in range(1, n):
        funcReconstructionGenerator = funcReconstructionGenerator + \
            Ak[i]*np.cos(i*Wo*timeReconstructionGenerator) + \
            Bk[i]*np.sin(i*Wo*timeReconstructionGenerator)
    funcReconstructionGenerator = funcReconstructionGenerator+A0
    timeReconstructionGenerator = timeReconstructionGenerator-T
    timeReconstructionGenerator = timeReconstructionGenerator/T*TFuncStatus

    plt.figure(figsize=(9, 9))
    plt.subplot(2, 2, 1)
    plt.title(nameFunc)
    plt.plot(tcarry, funcCarry)
    plt.subplot(2, 2, 2)
    plt.title('signal reconstruction')
    plt.plot(timeReconstructionGenerator, funcReconstructionGenerator)
    plt.subplot(2, 2, 3)
    plt.title('Phase Specter')
    plt.stem(Nk, Phi_k)
    plt.subplot(2, 2, 4)
    plt.title('Magnitud Specter')
    plt.stem(Nk, Ck)
    plt.show()


btnframe_X = Button(main, text="Graph", command=Action)
btnframe_X.place(y=280, x=20)
btnframe_X.configure(width=20, background='gainsboro')

main.mainloop()
