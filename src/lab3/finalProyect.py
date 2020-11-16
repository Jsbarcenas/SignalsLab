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

main = Tk()
main.title('Final Proyect')
main.configure(background='gainsboro', padx=30, pady=10)
main.geometry('1500x600')
main.resizable(0, 0)


emgFile = None

titleLab = Label(main, text="Muscle Signals Analitics")
titleLab.configure(width=30, background='gainsboro')
titleLab.place(y=20, x=270)

emgFileName = Entry(main, font=40)
emgFileName.configure(width=15)
emgFileName.place(y=70, x=140)

accFileName = Entry(main, font=40)
accFileName.configure(width=15)
accFileName.place(y=100, x=140)


isFatigatedLabACC = Label(main, text="Is fatigated?")
isFatigatedLabACC.configure(width=10, background='gainsboro', relief='groove')
isFatigatedLabACC.place(y=100, x=300)

isFatigatedEntryACC = Entry(main, font=40)
isFatigatedEntryACC.configure(width=4)
isFatigatedEntryACC.place(y=100, x=400)

isFatigatedLabEMG = Label(main, text="Is fatigated?")
isFatigatedLabEMG.configure(width=10, background='gainsboro', relief='groove')
isFatigatedLabEMG.place(y=70, x=300)

isFatigatedEntryEMG = Entry(main, font=40)
isFatigatedEntryEMG.configure(width=4)
isFatigatedEntryEMG.place(y=70, x=400)


def emgCallFile():
    global emgFile
    emgFileSelector = askopenfilename()
    emgFile, fs = sf.read(emgFileSelector)
    emgFileName.delete(0, END)
    emgFileName.insert(END, os.path.basename(emgFileSelector))


def accCallFile():
    global accFile
    accFileSelector = askopenfilename()
    accFile, fs1 = sf.read(accFileSelector)
    accFileName.delete(0, END)
    accFileName.insert(END, os.path.basename(accFileSelector))


selectEmgBtn = Button(main, text='Select EMG file', command=emgCallFile)
selectEmgBtn.configure(width=15, background='gainsboro')
selectEmgBtn.place(y=70, x=20)

selectAccBtn = Button(main, text='Select ACC file', command=accCallFile)
selectAccBtn.configure(width=15, bg='gainsboro')
selectAccBtn.place(y=100, x=20)


def GraphFunctions():
    global emgFileFftMag
    global accFileFftMag
    global emgFileFftFreq
    global accFileFftFreq

    emgFileFftMag = np.abs(np.fft.fft(emgFile))
    emgFileFftFreq = np.fft.fftfreq(len(emgFile))

    accFileFftMag = np.abs(np.fft.fft(accFile))
    accFileFftFreq = np.fft.fftfreq(len(accFile))

    print(emgFile)

    plt.figure(1)
    plt.clf()
    plt.title('EMG')
    plt.plot(emgFile)
    plt.gcf().canvas.draw()

    plt.figure(2)
    plt.clf()
    plt.title('ACC')
    plt.plot(accFile)
    plt.gcf().canvas.draw()

    plt.figure(3)
    plt.clf()
    plt.title('EMG Freq')
    plt.plot(emgFileFftFreq, emgFileFftMag)
    plt.gcf().canvas.draw()

    plt.figure(4)
    plt.clf()
    plt.title('ACC Freq')
    plt.plot(accFileFftFreq, accFileFftMag)
    plt.gcf().canvas.draw()


fig_1 = plt.figure(figsize=(5, 2),  dpi=60)
canv_1 = FigureCanvasTkAgg(fig_1, master=main)
canv_1.get_tk_widget().place(y=170, x=20)

fig_2 = plt.figure(figsize=(5, 2),  dpi=60)
canv_2 = FigureCanvasTkAgg(fig_2, master=main)
canv_2.get_tk_widget().place(y=320, x=20)

fig_3 = plt.figure(figsize=(5, 2),  dpi=60)
canv_3 = FigureCanvasTkAgg(fig_3, master=main)
canv_3.get_tk_widget().place(y=170, x=335)

fig_4 = plt.figure(figsize=(5, 2),  dpi=60)
canv_4 = FigureCanvasTkAgg(fig_4, master=main)
canv_4.get_tk_widget().place(y=320, x=335)

GraphFunctionsBtn = Button(
    main, text='Graph Functions', command=GraphFunctions)
GraphFunctionsBtn.configure(width=15, background='gainsboro')
GraphFunctionsBtn.place(y=130, x=20)


# Labels for information ACC MAG


accMagMediaLab = Label(main, text="Media")
accMagMediaLab.configure(width=10, background='gainsboro', relief='groove')
accMagMediaLab.place(y=70, x=650)

accMagMediaEntry = Entry(main, font=40)
accMagMediaEntry.configure(width=10)
accMagMediaEntry.place(y=70, x=730)

accMagMedianLab = Label(main, text="Median")
accMagMedianLab.configure(width=10, background='gainsboro', relief='groove')
accMagMedianLab.place(y=100, x=650)

accMagMedianEntry = Entry(main, font=40)
accMagMedianEntry.configure(width=10)
accMagMedianEntry.place(y=100, x=730)

accMagStandDeviLab = Label(main, text="STD Deviation")
accMagStandDeviLab.configure(width=10, background='gainsboro', relief='groove')
accMagStandDeviLab.place(y=130, x=650)

accMagStandDeviEntry = Entry(main, font=40)
accMagStandDeviEntry.configure(width=10)
accMagStandDeviEntry.place(y=130, x=730)

accMagAbsDeviLab = Label(main, text="ABS Deviation")
accMagAbsDeviLab.configure(width=10, background='gainsboro', relief='groove')
accMagAbsDeviLab.place(y=160, x=650)

accMagAbsDeviEntry = Entry(main, font=40)
accMagAbsDeviEntry.configure(width=10)
accMagAbsDeviEntry.place(y=160, x=730)

accMagQ1Lab = Label(main, text="Q1")
accMagQ1Lab.configure(width=10, background='gainsboro', relief='groove')
accMagQ1Lab.place(y=190, x=650)

accMagQ1Entry = Entry(main, font=40)
accMagQ1Entry.configure(width=10)
accMagQ1Entry.place(y=190, x=730)

accMagQ3Lab = Label(main, text="Q3")
accMagQ3Lab.configure(width=10, background='gainsboro', relief='groove')
accMagQ3Lab.place(y=220, x=650)

accMagQ3Entry = Entry(main, font=40)
accMagQ3Entry.configure(width=10)
accMagQ3Entry.place(y=220, x=730)

accMagIqrLab = Label(main, text="Iqr")
accMagIqrLab.configure(width=10, background='gainsboro', relief='groove')
accMagIqrLab.place(y=250, x=650)

accMagIqrEntry = Entry(main, font=40)
accMagIqrEntry.configure(width=10)
accMagIqrEntry.place(y=250, x=730)

accMagAsymmetryLab = Label(main, text="Asymmetry")
accMagAsymmetryLab.configure(width=10, background='gainsboro', relief='groove')
accMagAsymmetryLab.place(y=280, x=650)

accMagAsymmetryEntry = Entry(main, font=40)
accMagAsymmetryEntry.configure(width=10)
accMagAsymmetryEntry.place(y=280, x=730)

accMagKurtLab = Label(main, text="Kurtosis")
accMagKurtLab.configure(width=10, background='gainsboro', relief='groove')
accMagKurtLab.place(y=310, x=650)

accMagKurtEntry = Entry(main, font=40)
accMagKurtEntry.configure(width=10)
accMagKurtEntry.place(y=310, x=730)

accMagVarCoeLab = Label(main, text="Var.Coe")
accMagVarCoeLab.configure(width=10, background='gainsboro', relief='groove')
accMagVarCoeLab.place(y=340, x=650)

accMagVarCoeEntry = Entry(main, font=40)
accMagVarCoeEntry.configure(width=10)
accMagVarCoeEntry.place(y=340, x=730)

accMagPotencyLab = Label(main, text="Potency")
accMagPotencyLab.configure(width=10, background='gainsboro', relief='groove')
accMagPotencyLab.place(y=370, x=650)

accMagPotencyEntry = Entry(main, font=40)
accMagPotencyEntry.configure(width=10)
accMagPotencyEntry.place(y=370, x=730)

accMagTitleLab = Label(main, text="accMag Inf")
accMagTitleLab.configure(width=10, background='gainsboro', relief='groove')
accMagTitleLab.place(y=25, x=710)


# Labels for ACC FREQ


accFreqMediaLab = Label(main, text="Media")
accFreqMediaLab.configure(width=10, background='gainsboro', relief='groove')
accFreqMediaLab.place(y=70, x=840)

accFreqMediaEntry = Entry(main, font=40)
accFreqMediaEntry.configure(width=10)
accFreqMediaEntry.place(y=70, x=920)

accFreqMedianLab = Label(main, text="Median")
accFreqMedianLab.configure(width=10, background='gainsboro', relief='groove')
accFreqMedianLab.place(y=100, x=840)

accFreqMedianEntry = Entry(main, font=40)
accFreqMedianEntry.configure(width=10)
accFreqMedianEntry.place(y=100, x=920)

accFreqStandDeviLab = Label(main, text="STD Deviation")
accFreqStandDeviLab.configure(
    width=10, background='gainsboro', relief='groove')
accFreqStandDeviLab.place(y=130, x=840)

accFreqStandDeviEntry = Entry(main, font=40)
accFreqStandDeviEntry.configure(width=10)
accFreqStandDeviEntry.place(y=130, x=920)

accFreqAbsDeviLab = Label(main, text="ABS Deviation")
accFreqAbsDeviLab.configure(width=10, background='gainsboro', relief='groove')
accFreqAbsDeviLab.place(y=160, x=840)

accFreqAbsDeviEntry = Entry(main, font=40)
accFreqAbsDeviEntry.configure(width=10)
accFreqAbsDeviEntry.place(y=160, x=920)

accFreqQ1Lab = Label(main, text="Q1")
accFreqQ1Lab.configure(width=10, background='gainsboro', relief='groove')
accFreqQ1Lab.place(y=190, x=840)

accFreqQ1Entry = Entry(main, font=40)
accFreqQ1Entry.configure(width=10)
accFreqQ1Entry.place(y=190, x=920)

accFreqQ3Lab = Label(main, text="Q3")
accFreqQ3Lab.configure(width=10, background='gainsboro', relief='groove')
accFreqQ3Lab.place(y=220, x=840)

accFreqQ3Entry = Entry(main, font=40)
accFreqQ3Entry.configure(width=10)
accFreqQ3Entry.place(y=220, x=920)

accFreqIqrLab = Label(main, text="Iqr")
accFreqIqrLab.configure(width=10, background='gainsboro', relief='groove')
accFreqIqrLab.place(y=250, x=840)

accFreqIqrEntry = Entry(main, font=40)
accFreqIqrEntry.configure(width=10)
accFreqIqrEntry.place(y=250, x=920)

accFreqAsymmetryLab = Label(main, text="Asymmetry")
accFreqAsymmetryLab.configure(
    width=10, background='gainsboro', relief='groove')
accFreqAsymmetryLab.place(y=280, x=840)

accFreqAsymmetryEntry = Entry(main, font=40)
accFreqAsymmetryEntry.configure(width=10)
accFreqAsymmetryEntry.place(y=280, x=920)

accFreqKurtLab = Label(main, text="Kurt")
accFreqKurtLab.configure(width=10, background='gainsboro', relief='groove')
accFreqKurtLab.place(y=310, x=840)

accFreqKurtEntry = Entry(main, font=40)
accFreqKurtEntry.configure(width=10)
accFreqKurtEntry.place(y=310, x=920)

accFreqVarCoeLab = Label(main, text="Var.Coe")
accFreqVarCoeLab.configure(width=10, background='gainsboro', relief='groove')
accFreqVarCoeLab.place(y=340, x=840)

accFreqVarCoeEntry = Entry(main, font=40)
accFreqVarCoeEntry.configure(width=10)
accFreqVarCoeEntry.place(y=340, x=920)

accFreqPotencyLab = Label(main, text="Potency")
accFreqPotencyLab.configure(width=10, background='gainsboro', relief='groove')
accFreqPotencyLab.place(y=370, x=840)

accFreqPotencyEntry = Entry(main, font=40)
accFreqPotencyEntry.configure(width=10)
accFreqPotencyEntry.place(y=370, x=920)

accFreqTitleLab = Label(main, text="ACC Freq Inf")
accFreqTitleLab.configure(width=10, background='gainsboro', relief='groove')
accFreqTitleLab.place(y=25, x=890)


# Labels for Information EMG MAG


emgMagMediaLab = Label(main, text="Media")
emgMagMediaLab.configure(width=10, background='gainsboro', relief='groove')
emgMagMediaLab.place(y=70, x=1050)

emgMagMediaEntry = Entry(main, font=40)
emgMagMediaEntry.configure(width=10)
emgMagMediaEntry.place(y=70, x=1130)

emgMagMedianLab = Label(main, text="Median")
emgMagMedianLab.configure(width=10, background='gainsboro', relief='groove')
emgMagMedianLab.place(y=100, x=1050)

emgMagMedianEntry = Entry(main, font=40)
emgMagMedianEntry.configure(width=10)
emgMagMedianEntry.place(y=100, x=1130)

emgMagStandDeviLab = Label(main, text="STD Deviation")
emgMagStandDeviLab.configure(width=10, background='gainsboro', relief='groove')
emgMagStandDeviLab.place(y=130, x=1050)

emgMagStandDeviEntry = Entry(main, font=40)
emgMagStandDeviEntry.configure(width=10)
emgMagStandDeviEntry.place(y=130, x=1130)

emgMagAbsDeviLab = Label(main, text="ABS Deviation")
emgMagAbsDeviLab.configure(width=10, background='gainsboro', relief='groove')
emgMagAbsDeviLab.place(y=160, x=1050)

emgMagAbsDeviEntry = Entry(main, font=40)
emgMagAbsDeviEntry.configure(width=10)
emgMagAbsDeviEntry.place(y=160, x=1130)

emgMagQ1Lab = Label(main, text="Q1")
emgMagQ1Lab.configure(width=10, background='gainsboro', relief='groove')
emgMagQ1Lab.place(y=190, x=1050)

emgMagQ1Entry = Entry(main, font=40)
emgMagQ1Entry.configure(width=10)
emgMagQ1Entry.place(y=190, x=1130)

emgMagQ3Lab = Label(main, text="Q3")
emgMagQ3Lab.configure(width=10, background='gainsboro', relief='groove')
emgMagQ3Lab.place(y=220, x=1050)

emgMagQ3Entry = Entry(main, font=40)
emgMagQ3Entry.configure(width=10)
emgMagQ3Entry.place(y=220, x=1130)

emgMagIqrLab = Label(main, text="Iqr")
emgMagIqrLab.configure(width=10, background='gainsboro', relief='groove')
emgMagIqrLab.place(y=250, x=1050)

emgMagIqrEntry = Entry(main, font=40)
emgMagIqrEntry.configure(width=10)
emgMagIqrEntry.place(y=250, x=1130)

emgMagAsymmetryLab = Label(main, text="Asymmetry")
emgMagAsymmetryLab.configure(width=10, background='gainsboro', relief='groove')
emgMagAsymmetryLab.place(y=280, x=1050)

emgMagAsymmetryEntry = Entry(main, font=40)
emgMagAsymmetryEntry.configure(width=10)
emgMagAsymmetryEntry.place(y=280, x=1130)

emgMagKurtLab = Label(main, text="Kurtosis")
emgMagKurtLab.configure(width=10, background='gainsboro', relief='groove')
emgMagKurtLab.place(y=310, x=1050)

emgMagKurtEntry = Entry(main, font=40)
emgMagKurtEntry.configure(width=10)
emgMagKurtEntry.place(y=310, x=1130)

emgMagVarCoeLab = Label(main, text="Var.Coe")
emgMagVarCoeLab.configure(width=10, background='gainsboro', relief='groove')
emgMagVarCoeLab.place(y=340, x=1050)

emgMagVarCoeEntry = Entry(main, font=40)
emgMagVarCoeEntry.configure(width=10)
emgMagVarCoeEntry.place(y=340, x=1130)

emgMagPotencyLab = Label(main, text="Potency")
emgMagPotencyLab.configure(width=10, background='gainsboro', relief='groove')
emgMagPotencyLab.place(y=370, x=1050)

emgMagPotencyEntry = Entry(main, font=40)
emgMagPotencyEntry.configure(width=10)
emgMagPotencyEntry.place(y=370, x=1130)

emgFreqTitleLab = Label(main, text="EMG Mag Inf")
emgFreqTitleLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqTitleLab.place(y=25, x=1120)


# label for info EMG FREQ

emgFreqMediaLab = Label(main, text="Media")
emgFreqMediaLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqMediaLab.place(y=70, x=1250)

emgFreqMediaEntry = Entry(main, font=40)
emgFreqMediaEntry.configure(width=10)
emgFreqMediaEntry.place(y=70, x=1330)

emgFreqMedianLab = Label(main, text="Median")
emgFreqMedianLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqMedianLab.place(y=100, x=1250)

emgFreqMedianEntry = Entry(main, font=40)
emgFreqMedianEntry.configure(width=10)
emgFreqMedianEntry.place(y=100, x=1330)

emgFreqStandDeviLab = Label(main, text="STD Deviation")
emgFreqStandDeviLab.configure(
    width=10, background='gainsboro', relief='groove')
emgFreqStandDeviLab.place(y=130, x=1250)

emgFreqStandDeviEntry = Entry(main, font=40)
emgFreqStandDeviEntry.configure(width=10)
emgFreqStandDeviEntry.place(y=130, x=1330)

emgFreqAbsDeviLab = Label(main, text="ABS Deviation")
emgFreqAbsDeviLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqAbsDeviLab.place(y=160, x=1250)

emgFreqAbsDeviEntry = Entry(main, font=40)
emgFreqAbsDeviEntry.configure(width=10)
emgFreqAbsDeviEntry.place(y=160, x=1330)

emgFreqQ1Lab = Label(main, text="Q1")
emgFreqQ1Lab.configure(width=10, background='gainsboro', relief='groove')
emgFreqQ1Lab.place(y=190, x=1250)

emgFreqQ1Entry = Entry(main, font=40)
emgFreqQ1Entry.configure(width=10)
emgFreqQ1Entry.place(y=190, x=1330)

emgFreqQ3Lab = Label(main, text="Q3")
emgFreqQ3Lab.configure(width=10, background='gainsboro', relief='groove')
emgFreqQ3Lab.place(y=220, x=1250)

emgFreqQ3Entry = Entry(main, font=40)
emgFreqQ3Entry.configure(width=10)
emgFreqQ3Entry.place(y=220, x=1330)

emgFreqIqrLab = Label(main, text="Iqr")
emgFreqIqrLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqIqrLab.place(y=250, x=1250)

emgFreqIqrEntry = Entry(main, font=40)
emgFreqIqrEntry.configure(width=10)
emgFreqIqrEntry.place(y=250, x=1330)

emgFreqAsymmetryLab = Label(main, text="Asymmetry")
emgFreqAsymmetryLab.configure(
    width=10, background='gainsboro', relief='groove')
emgFreqAsymmetryLab.place(y=280, x=1250)

emgFreqAsymmetryEntry = Entry(main, font=40)
emgFreqAsymmetryEntry.configure(width=10)
emgFreqAsymmetryEntry.place(y=280, x=1330)

emgFreqKurtLab = Label(main, text="Kurt")
emgFreqKurtLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqKurtLab.place(y=310, x=1250)

emgFreqKurtEntry = Entry(main, font=40)
emgFreqKurtEntry.configure(width=10)
emgFreqKurtEntry.place(y=310, x=1330)

emgFreqVarCoeLab = Label(main, text="Var.Coe")
emgFreqVarCoeLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqVarCoeLab.place(y=340, x=1250)

emgFreqVarCoeEntry = Entry(main, font=40)
emgFreqVarCoeEntry.configure(width=10)
emgFreqVarCoeEntry.place(y=340, x=1330)

emgFreqPotencyLab = Label(main, text="Potency")
emgFreqPotencyLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqPotencyLab.place(y=370, x=1250)

emgFreqPotencyEntry = Entry(main, font=40)
emgFreqPotencyEntry.configure(width=10)
emgFreqPotencyEntry.place(y=370, x=1330)

emgFreqTitleLab = Label(main, text="emg Freq Inf")
emgFreqTitleLab.configure(width=10, background='gainsboro', relief='groove')
emgFreqTitleLab.place(y=25, x=1280)


def dispatch():
    accShowValues()
    emgShowVAlues()


def accShowValues():
    # MAG

    accMagMediaEntry.delete(0, END)
    accMagMedianEntry.delete(0, END)
    accMagStandDeviEntry.delete(0, END)
    accMagAbsDeviEntry.delete(0, END)
    accMagQ1Entry.delete(0, END)
    accMagQ3Entry.delete(0, END)
    accMagIqrEntry.delete(0, END)
    accMagAsymmetryEntry.delete(0, END)
    accMagKurtEntry.delete(0, END)
    accMagVarCoeEntry.delete(0, END)
    accMagPotencyEntry.delete(0, END)

    accFreqMediaEntry.delete(0, END)
    accFreqMedianEntry.delete(0, END)
    accFreqStandDeviEntry.delete(0, END)
    accFreqAbsDeviEntry.delete(0, END)
    accFreqQ1Entry.delete(0, END)
    accFreqQ3Entry.delete(0, END)
    accFreqIqrEntry.delete(0, END)
    accFreqAsymmetryEntry.delete(0, END)
    accFreqKurtEntry.delete(0, END)
    accFreqVarCoeEntry.delete(0, END)
    accFreqPotencyEntry.delete(0, END)

    accMagMediaEntry.insert(END, st.Media2(accFile))
    accMagMedianEntry.insert(END, st.median(accFile))
    accMagStandDeviEntry.insert(END, st.variance(accFile))
    accMagAbsDeviEntry.insert(END, st.varianceABS(accFile))
    accMagQ1Entry.insert(END, st.q1(accFile))
    accMagQ3Entry.insert(END, st.q3(accFile))
    accMagIqrEntry.insert(END, st.iqr(accFile))
    accMagAsymmetryEntry.insert(END, st.asymmetry(accFile))
    accMagKurtEntry.insert(END, st.Kurtosis(accFile))
    accMagVarCoeEntry.insert(END, st.CoeficienteVariacion(accFile))
    accMagPotencyEntry.insert(END, st.potency(accFile))
    # Freq
    accFreqMediaEntry.insert(END, st.media(accFileFftMag))
    accFreqMedianEntry.insert(END, st.median(accFileFftMag))
    accFreqStandDeviEntry.insert(END, st.variance(accFileFftMag))
    accFreqAbsDeviEntry.insert(END, st.varianceABS(accFileFftMag))
    accFreqQ1Entry.insert(END, st.q1(accFileFftMag))
    accFreqQ3Entry.insert(END, st.q3(accFileFftMag))
    accFreqIqrEntry.insert(END, st.iqr(accFileFftMag))
    accFreqAsymmetryEntry.insert(END, st.asymmetry(accFileFftMag))
    accFreqKurtEntry.insert(END, st.Kurtosis(accFileFftMag))
    accFreqVarCoeEntry.insert(END, st.CoeficienteVariacion(accFileFftMag))
    accFreqPotencyEntry.insert(END, st.potency(accFileFftMag))


def emgShowVAlues():

    emgMagMediaEntry.delete(0, END)
    emgMagMedianEntry.delete(0, END)
    emgMagStandDeviEntry.delete(0, END)
    emgMagAbsDeviEntry.delete(0, END)
    emgMagQ1Entry.delete(0, END)
    emgMagQ3Entry.delete(0, END)
    emgMagIqrEntry.delete(0, END)
    emgMagAsymmetryEntry.delete(0, END)
    emgMagKurtEntry.delete(0, END)
    emgMagVarCoeEntry.delete(0, END)
    emgMagPotencyEntry.delete(0, END)

    emgFreqMediaEntry.delete(0, END)
    emgFreqMedianEntry.delete(0, END)
    emgFreqStandDeviEntry.delete(0, END)
    emgFreqAbsDeviEntry.delete(0, END)
    emgFreqQ1Entry.delete(0, END)
    emgFreqQ3Entry.delete(0, END)
    emgFreqIqrEntry.delete(0, END)
    emgFreqAsymmetryEntry.delete(0, END)
    emgFreqKurtEntry.delete(0, END)
    emgFreqVarCoeEntry.delete(0, END)
    emgFreqPotencyEntry.delete(0, END)

    emgMagMediaEntry.insert(END, st.media(emgFile))
    emgMagMedianEntry.insert(END, st.median(emgFile))
    emgMagStandDeviEntry.insert(END, st.variance(emgFile))
    emgMagAbsDeviEntry.insert(END, st.varianceABS(emgFile))
    emgMagQ1Entry.insert(END, st.q1(emgFile))
    emgMagQ3Entry.insert(END, st.q3(emgFile))
    emgMagIqrEntry.insert(END, st.iqr(emgFile))
    emgMagAsymmetryEntry.insert(END, st.asymmetry(emgFile))
    emgMagKurtEntry.insert(END, st.Kurtosis(emgFile))
    emgMagVarCoeEntry.insert(END, st.CoeficienteVariacion(emgFile))
    emgMagPotencyEntry.insert(END, st.potency(emgFile))
    # Freq
    emgFreqMediaEntry.insert(END, st.media(emgFileFftMag))
    emgFreqMedianEntry.insert(END, st.median(emgFileFftMag))
    emgFreqStandDeviEntry.insert(END, st.variance(emgFileFftMag))
    emgFreqAbsDeviEntry.insert(END, st.varianceABS(emgFileFftMag))
    emgFreqQ1Entry.insert(END, st.q1(emgFileFftMag))
    emgFreqQ3Entry.insert(END, st.q3(emgFileFftMag))
    emgFreqIqrEntry.insert(END, st.iqr(emgFileFftMag))
    emgFreqAsymmetryEntry.insert(END, st.asymmetry(emgFileFftMag))
    emgFreqKurtEntry.insert(END, st.Kurtosis(emgFileFftMag))
    emgFreqVarCoeEntry.insert(END, st.CoeficienteVariacion(emgFileFftMag))
    emgFreqPotencyEntry.insert(END, st.potency(emgFileFftMag))


showValueBtn = Button(
    main, text='Show Values', command=dispatch)
showValueBtn.configure(width=15, background='gainsboro')
showValueBtn.place(y=130, x=140)


def isFatigated():
    if st.potency(emgFileFftMag) < 100:
        F = 0
        N = 0
        if st.potency(emgFileFftMag) > 20:
            F = F + 1
            N = N + 0
        if st.Kurtosis(emgFile) < 10:
            F = F + 1
            N = N + 0
        if st.potency(emgFileFftMag) < 20:
            N = N + 1
            F = F + 0
        if st.Kurtosis(emgFile) > 10:
            N = N + 1
            F = F + 0
        if F == 2:
            isFatigatedEntryEMG.delete(0, END)
            isFatigatedEntryEMG.insert(END, 'SI')
            print('EMG Fatigada')

        if N == 2:
            isFatigatedEntryEMG.delete(0, END)
            isFatigatedEntryEMG.insert(END, 'NO')
            print('EMG no fatigada')
    if st.potency(accFileFftMag) < 100:
        F = 0
        N = 0
        if st.potency(accFileFftMag) > 20:
            F = F + 1
            N = N + 0
        if st.Kurtosis(accFile) < 10:
            F = F + 1
            N = N + 0
        if st.potency(accFileFftMag) < 20:
            N = N + 1
            F = F + 0
        if st.Kurtosis(accFile) > 10:
            N = N + 1
            F = F + 0
        if F == 2:
            isFatigatedEntryACC.delete(0, END)
            isFatigatedEntryACC.insert(END, 'Si')
            print('ACC fatigada')
        if N == 2:
            isFatigatedEntryACC.delete(0, END)
            isFatigatedEntryACC.insert(END, 'NO')
            print('ACC No fatigada')
    if st.potency(emgFileFftMag) > 100:

        if st.Kurtosis(emgFileFftMag) > 550 or st.Kurtosis(emgFile) > 2:
            isFatigatedEntryEMG.delete(0, END)
            isFatigatedEntryEMG.insert(END, 'NO')
            print('EMG NO Fatigada')

        else:
            isFatigatedEntryEMG.delete(0, END)
            isFatigatedEntryEMG.insert(END, 'SI')
            print('EMG Fatigada')
    if st.potency(accFileFftMag) > 100:

        if st.Kurtosis(accFileFftMag) > 550 or st.Kurtosis(accFile) > 2:
            isFatigatedEntryACC.delete(0, END)
            isFatigatedEntryACC.insert(END, 'NO')
            print('EMG NO Fatigada')
        else:
            isFatigatedEntryACC.delete(0, END)
            isFatigatedEntryACC.insert(END, 'SI')
            print('EMG Fatigada')


showFatiBtn = Button(
    main, text='Show Fatigated', command=isFatigated)
showFatiBtn.configure(width=15, background='gainsboro')
showFatiBtn.place(y=130, x=300)
mainloop()
