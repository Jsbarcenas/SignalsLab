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

main = Tk()
main.title('Final Proyect')
main.configure(background='gainsboro', padx=30, pady=10)
main.geometry('800x600')
main.resizable(0,0)


emgFile = None

titleLab = Label(main, text = "Muscle Signals Analitics")
titleLab.configure(width = 30, background = 'gainsboro')
titleLab.place(y= 20, x= 270)

emgFileName = Entry(main, font = 40)
emgFileName.configure(width = 15)
emgFileName.place(y = 70, x = 140)

accFileName = Entry(main, font = 40)
accFileName.configure(width = 15)
accFileName.place(y = 100, x = 140)


def emgCallFile() : 
    global emgFile
    emgFileSelector = askopenfilename()
    emgFile , fs= sf.read(emgFileSelector)
    emgFileName.insert(END, os.path.basename(emgFileSelector))

def accCallFile() : 
    global accFile
    accFileSelector= askopenfilename()
    accFile, fs = sf.read(accFileSelector)
    accFileName.insert(END, os.path.basename(accFileSelector))
    
    
   
 
selectEmgBtn = Button(main, text= 'Select EMG file', command = emgCallFile)
selectEmgBtn.configure(width = 15, background = 'gainsboro')
selectEmgBtn.place( y = 70, x =20)

selectAccBtn = Button(main, text = 'Select ACC file', command = accCallFile)
selectAccBtn.configure(width = 15, bg= 'gainsboro')
selectAccBtn.place(y = 100, x= 20)


def GraphFunctions(): 
    
    emgFileFftMag = np.abs(np.fft.fft(emgFile))
    emgFileFftFreq= np.fft.fftfreq(len(emgFile))

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
    plt.plot(emgFileFftFreq,emgFileFftMag)
    plt.gcf().canvas.draw()

    plt.figure(4)
    plt.clf()
    plt.title('ACC Freq')
    plt.plot(accFileFftFreq, accFileFftMag)
    plt.gcf().canvas.draw()

fig_1= plt.figure(figsize=(5, 2),  dpi = 60)
canv_1 = FigureCanvasTkAgg(fig_1, master=main)
canv_1.get_tk_widget().place( y = 170 , x = 20)

fig_2= plt.figure(figsize=(5, 2),  dpi = 60)
canv_2 = FigureCanvasTkAgg(fig_2, master=main)
canv_2.get_tk_widget().place( y = 320 , x = 20)

fig_3= plt.figure(figsize=(5, 2),  dpi = 60)
canv_3 = FigureCanvasTkAgg(fig_3, master=main)
canv_3.get_tk_widget().place(y = 170 , x =335)

fig_4= plt.figure(figsize=(5, 2),  dpi = 60)
canv_4 = FigureCanvasTkAgg(fig_4, master=main)
canv_4.get_tk_widget().place(y = 320 , x =335)

GraphFunctionsBtn= Button(main, text = 'Graph Functions', command = GraphFunctions)
GraphFunctionsBtn.configure(width = 15, background = 'gainsboro')
GraphFunctionsBtn.place(y =  130, x= 20)



mainloop()