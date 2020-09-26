##Bueno profe, aquí hoy, martes 22  a las 5:05 de la tarde comienzo con su laboratorio.
##Espero disfrute leyendo este código. ;)

import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from scipy import signal as sp
from tkinter import ttk





main = Tk()
main.config(bg = 'gainsboro')
main.geometry('610x540')
main.resizable(0,0)
main.title('Signal Convolutions')
titleLabel= Label(main, text = 'Laboratory 2th-- Signal Convolutions')
titleLabel.config( padx = 5, pady= 5, bg = 'gainsboro')
titleLabel.place(x = 200)

##Variable globales entry
amplitudF1Entry = None
periodF1Entry = None
exponentF1Entry = None

amplitudF2Entry = None
periodF2Entry = None
exponentF2Entry = None
timeInitF2Entry = None
timeFinalF2Entry = None
exponentF1Entry = None
timeInitF1Entry = None

figF1 = None
figF2 = None 
figF3 = None
canv = None
figuresNumber1 = 4
figuresNumber2 = 5
figuresNumber3 = 6
periodDef= 1

timeGeneratorF1 = np.arange(0,1,0.001)
plotF1GeneratorStatus = 1
plotF1TimeGeneratorStatus= 1

timeDomineStatus = 1

entryState = "disable"
entryStateE = "disable"

##Time domine logic

def changeTimeDomine(event):
    global timeDomineStatus
    if selecTimeDomineComb.get() == 'Continuous':
        timeDomineStatus = 1
        print(timeDomineStatus)
    else:
        timeDomineStatus = 0
        print(timeDomineStatus)
        


##Marcos de opcion 1
function1 = LabelFrame(main, text= 'x(t)/x[n]')
function1.config(width = 140, height = 50, bg = 'gainsboro')
function1.place(y= 50)
labelTitleF1= Label(function1, text = 'stand by function',pady= 10)
labelTitleF1.config(width= 40, bg = 'gainsboro')
labelTitleF1.grid(row = 0, column= 0)



def callbackF1ModEntry (event):
    global amplitudF1Entry
    global periodF1Entry
    global exponentF1Entry
    global timeInitF1Entry
    global timeFinalF1Entry
    if selectF1Lab.get() == "Exponential":
        amplitudF1Entry = Entry(function1, state = 'normal')
        amplitudF1Entry.config(bd = 2, width= 5)
        amplitudF1Entry.place( x = 60, y = 65)
        periodF1Entry = Entry(function1, state = 'disable')
        periodF1Entry.config(bg = 'white',bd = 2, width= 5)
        periodF1Entry.place( x = 60, y = 95)
        exponentF1Entry = Entry(function1, state = 'normal')
        exponentF1Entry.config(bg = 'white',bd = 2, width= 5)
        exponentF1Entry.place( x = 160, y = 65)
        timeInitF1Entry = Entry(function1, state ='normal')
        timeInitF1Entry.config(bg = 'white',bd = 2, width= 5)
        timeInitF1Entry.place( x = 160, y = 95)
        timeFinalF1Entry = Entry(function1, state = 'normal')
        timeFinalF1Entry.config(bg = 'white',bd = 2, width= 5)
        timeFinalF1Entry.place( x = 260, y = 95)
        
    else :
        amplitudF1Entry = Entry(function1, state = 'normal')
        amplitudF1Entry.config(bd = 2, width= 5)
        amplitudF1Entry.place( x = 60, y = 65)
        periodF1Entry = Entry(function1, state = 'normal')
        periodF1Entry.config(bg = 'white',bd = 2, width= 5)
        periodF1Entry.place( x = 60, y = 95)
        exponentF1Entry = Entry(function1, state = 'disable')
        exponentF1Entry.config(bg = 'white',bd = 2, width= 5)
        exponentF1Entry.place( x = 160, y = 65)
        timeInitF1Entry = Entry(function1, state ='normal')
        timeInitF1Entry.config(bg = 'white',bd = 2, width= 5)
        timeInitF1Entry.place( x = 160, y = 95)
        timeFinalF1Entry = Entry(function1, state = 'normal')
        timeFinalF1Entry.config(bg = 'white',bd = 2, width= 5)
        timeFinalF1Entry.place( x = 260, y = 95)
        

def GraphF1():
    global timeGeneratorF1
    global plotF1GeneratorStatus
    global plotF1TimeGeneratorStatus
    global periodDef
    global timeGeneratorF1Else
    print(timeDomineStatus)
    if timeDomineStatus == 1:
        if selectF1Lab.get() == 'Exponential':
            timeGeneratorExponetial = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),0.001)
            exponentialGenerator = np.exp(timeGeneratorExponetial*float(exponentF1Entry.get()))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus =  timeGeneratorExponetial
            plotF1GeneratorStatus = exponentialGenerator
            canvasChange()
            print(exponentialGenerator)
        if selectF1Lab.get() == 'Sinusoidal':
            periodDef =float(periodF1Entry.get())
            print(periodDef)
            timeGeneratorF1Else = np.arange(0,periodDef,0.0001)
            sinusoidalGenerator = (np.sin(2*np.pi*(timeGeneratorF1Else)))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus = timeGeneratorF1Else
            plotF1GeneratorStatus = sinusoidalGenerator
            canvasChange()
            print(sinusoidalGenerator)
        if selectF1Lab.get() == 'Triangular':
            periodDef =float(periodF1Entry.get())
            print(periodDef)
            timeGeneratorF1Else = np.arange(0,periodDef*6.3,0.0001)
            triangularGenerator = (sp.sawtooth(timeGeneratorF1Else))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus = timeGeneratorF1Else
            plotF1GeneratorStatus = triangularGenerator
            canvasChange()
            print(triangularGenerator)
        if selectF1Lab.get() == 'Rectangular':
            exponentialGenerator = np.exp(timeGeneratorF1*float(exponentF1Entry.get()))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus = timeGeneratorF1
            plotF1GeneratorStatus = exponentialGenerator
            canvasChange()
            print(exponentialGenerator)   
        if selectF1Lab.get() == 'Ramp1':
            exponentialGenerator = np.exp(timeGeneratorF1*float(exponentF1Entry.get()))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus = timeGeneratorF1
            plotF1GeneratorStatus = exponentialGenerator
            canvasChange()
            print(exponentialGenerator)
        if selectF1Lab.get() == 'Ramp2':
            exponentialGenerator = np.exp(timeGeneratorF1*float(exponentF1Entry.get()))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus = timeGeneratorF1
            plotF1GeneratorStatus = exponentialGenerator
            canvasChange()
            print(exponentialGenerator)
        if selectF1Lab.get() == 'Ramp3':
            exponentialGenerator = np.exp(timeGeneratorF1*float(exponentF1Entry.get()))*float(amplitudF1Entry.get())
            plotF1TimeGeneratorStatus = timeGeneratorF1
            plotF1GeneratorStatus = exponentialGenerator
            canvasChange()
            print(exponentialGenerator)                                     
    else: print('Haré otra cosa')

selectF1Lab = ttk.Combobox(function1, values = ["Exponential", "Sinusoidal", "Triangular",'Rectangular','Ramp1','Ramp2','Ramp3'],state="readonly")
selectF1Lab.grid(sticky = 'w', row= 1, column = 0)
selectF1Lab.bind("<<ComboboxSelected>>", callbackF1ModEntry)

amplitudF1lab = Label(function1, text = 'Amplitud')
amplitudF1lab.config(pady = 5, padx = 1, bg = 'gainsboro')
amplitudF1lab.grid(sticky = 'w', row = 2, column= 0)
amplitudF1Entry = Entry(function1, state = entryState)
amplitudF1Entry.config(bd = 2, width= 5)
amplitudF1Entry.place( x = 60, y = 65)

periodF1Lab= Label(function1, text ="Period")
periodF1Lab.config(pady = 5, padx = 1, bg = 'gainsboro')
periodF1Lab.grid(sticky = 'w', row = 3, column= 0)
periodF1Entry = Entry(function1, state = entryState)
periodF1Entry.config(bg = 'white',bd = 2, width= 5)
periodF1Entry.place( x = 60, y = 95)

exponentF1Lab= Label(function1, text ="Exponent")
exponentF1Lab.config(pady = 5, padx = 1, bg= 'gainsboro')
exponentF1Lab.place(x= 100, y = 60)
exponentF1Entry = Entry(function1, state = entryStateE)
exponentF1Entry.config(bg = 'white',bd = 2, width= 5)
exponentF1Entry.place( x = 160, y = 65)

timeInitF1Lab= Label(function1, text ="Time Init")
timeInitF1Lab.config(pady = 4, padx = 1, bg ='gainsboro')
timeInitF1Lab.place(x= 100, y = 90)
timeInitF1Entry = Entry(function1, state = entryStateE)
timeInitF1Entry.config(bg = 'white',bd = 2, width= 5)
timeInitF1Entry.place( x = 160, y = 95)

timeFinalF1Lab= Label(function1, text ="Time Final")
timeFinalF1Lab.config(pady = 4, padx = 1, bg ='gainsboro')
timeFinalF1Lab.place(x= 200, y = 90)
timeFinalF1Entry = Entry(function1, state = entryStateE)
timeFinalF1Entry.config(bg = 'white',bd = 2, width= 5)
timeFinalF1Entry.place( x = 260, y = 95)





##Marco de opcion 2
function2 = LabelFrame(main, text= 'h(t)/h[n]')
function2.config(width = 140, height = 50, bg = 'gainsboro')
function2.place(y= 50, x = 310)
labelTitleF2= Label(function2, text = 'Moving Function',pady= 10)
labelTitleF2.config(width= 40, bg = 'gainsboro')
labelTitleF2.grid(row = 0, column= 0)

def callbackF2ModEntry (event):
    global amplitudF2Entry
    global periodF2Entry
    global exponentF2Entry
    global timeInitF2Entry
    global timeFinalF2Entry
    if selectF2Lab.get() == "Exponential":
        amplitudF1Entry = Entry(function2, state = 'normal')
        amplitudF1Entry.config(bd = 2, width= 5)
        amplitudF1Entry.place( x = 60, y = 65)
        periodF1Entry = Entry(function2, state = 'disable')
        periodF1Entry.config(bg = 'white',bd = 2, width= 5)
        periodF1Entry.place( x = 60, y = 95)
        exponentF1Entry = Entry(function2, state = 'normal')
        exponentF1Entry.config(bg = 'white',bd = 2, width= 5)
        exponentF1Entry.place( x = 160, y = 65)
        timeInitF2Entry = Entry(function2, state = 'normal')
        timeInitF2Entry.config(bg = 'white',bd = 2, width= 5)
        timeInitF2Entry.place( x = 160, y = 95)
        timeFinalF2Entry = Entry(function2, state = 'normal')
        timeFinalF2Entry.config(bg = 'white',bd = 2, width= 5)
        timeFinalF2Entry.place( x = 260, y = 95)

    else :
        amplitudF1Entry = Entry(function2, state = 'normal')
        amplitudF1Entry.config(bd = 2, width= 5)
        amplitudF1Entry.place( x = 60, y = 65)
        periodF1Entry = Entry(function2, state = 'normal')
        periodF1Entry.config(bg = 'white',bd = 2, width= 5)
        periodF1Entry.place( x = 60, y = 95)
        exponentF1Entry = Entry(function2, state = 'disable')
        exponentF1Entry.config(bg = 'white',bd = 2, width= 5)
        exponentF1Entry.place( x = 160, y = 65)
        timeInitF2Entry = Entry(function2, state = 'normal')
        timeInitF2Entry.config(bg = 'white',bd = 2, width= 5)
        timeInitF2Entry.place( x = 160, y = 95)
        timeFinalF2Entry = Entry(function2, state = 'normal')
        timeFinalF2Entry.config(bg = 'white',bd = 2, width= 5)
        timeFinalF2Entry.place( x = 260, y = 95)


       
selectF2Lab = ttk.Combobox(function2, values = ["Exponential", "Sinusoidal", "Triangular",'Rectangular','Ramp1','Ramp2','Ramp3'],state="readonly")
selectF2Lab.grid(sticky = 'w', row= 1, column = 0)
selectF2Lab.bind("<<ComboboxSelected>>", callbackF2ModEntry)

amplitudF2lab = Label(function2, text = 'Amplitud')
amplitudF2lab.config(pady = 5, padx = 1,  bg ='gainsboro')
amplitudF2lab.grid(sticky = 'w', row = 2, column= 0)
amplitudF2Entry = Entry(function2, state = entryState)
amplitudF2Entry.config(bd = 2, width= 5)
amplitudF2Entry.place( x = 60, y = 65)

periodF2Lab= Label(function2, text ="Period")
periodF2Lab.config(pady = 5, padx = 1, bg = 'gainsboro')
periodF2Lab.grid(sticky = 'w', row = 3, column= 0)
periodF2Entry = Entry(function2, state = entryState)
periodF2Entry.config(bg = 'white',bd = 2, width= 5)
periodF2Entry.place( x = 60, y = 95)

exponentF2Lab= Label(function2, text ="Exponent")
exponentF2Lab.config(pady = 5, padx = 1, bg = 'gainsboro')
exponentF2Lab.place(x= 100, y = 60)
exponentF2Entry = Entry(function2, state = entryStateE)
exponentF2Entry.config(bg = 'white',bd = 2, width= 5)
exponentF2Entry.place( x = 160, y = 65)

timeInitF2Lab= Label(function2, text ="Time Init")
timeInitF2Lab.config(pady = 4, padx = 1, bg ='gainsboro')
timeInitF2Lab.place(x= 100, y = 90)
timeInitF2Entry = Entry(function2, state = entryStateE)
timeInitF2Entry.config(bg = 'white',bd = 2, width= 5)
timeInitF2Entry.place( x = 160, y = 95)

timeFinalF2Lab= Label(function2, text ="Time Final")
timeFinalF2Lab.config(pady = 4, padx = 1, bg ='gainsboro')
timeFinalF2Lab.place(x= 200, y = 90)
timeFinalF2Entry = Entry(function2, state = entryStateE)
timeFinalF2Entry.config(bg = 'white',bd = 2, width= 5)
timeFinalF2Entry.place( x = 260, y = 95)

##Canvas declaration and rewriting

def canvasChange():
    global plotF1GeneratorStatus
    global plotF1TimeGeneratorStatus
    global figF1
    global figF2
    global figF3
    global canv
    global figuresNumber1 
    global figuresNumber2
    global figuresNumber3

 
    plt.figure(1)
    plt.clf()
    plt.plot(plotF1TimeGeneratorStatus, plotF1GeneratorStatus)
    plt.gcf().canvas.draw()
 
    plt.figure(2)
    plt.clf()
    plt.plot(2,2)
    plt.gcf().canvas.draw()

    plt.figure(3)
    plt.clf()
    plt.figure(6)
    plt.plot(2,2)
    plt.gcf().canvas.draw()

figF1 = plt.figure(figsize=(4.5, 2), facecolor ="gainsboro",dpi = 72)
canv = FigureCanvasTkAgg(figF1, master=main)
canv.get_tk_widget().place(x = 0, y= 215)
plt.clf()
plt.figure(1)
plt.plot(1,1)
plt.gcf().canvas.draw()

figF2 = plt.figure(figsize=(4.5, 2), facecolor ="gainsboro", dpi = 72)
canv = FigureCanvasTkAgg(figF2, master=main)
canv.get_tk_widget().place(x = 305, y= 215)
plt.clf()
plt.figure(2)
plt.plot(2,2)
plt.gcf().canvas.draw()

figF3 = plt.figure(figsize=(10, 2), facecolor ="gainsboro", dpi = 72)
canv = FigureCanvasTkAgg(figF3, master=main)
canv.get_tk_widget().place(x = -53, y= 380)
plt.clf()
plt.figure(3)
plt.plot(2,2)
plt.gcf().canvas.draw()

selecTimeDomineComb = ttk.Combobox(main, values = ['Continuous','Discrete'],state="readonly")
selecTimeDomineComb.place(x = 150, y= 195)
selecTimeDomineComb.current(0)
selecTimeDomineComb.bind("<<ComboboxSelected>>", changeTimeDomine)

selectTimeDomineLab = Label(main, text = 'Select Time Domine')
selectTimeDomineLab.configure(bg= 'gainsboro')
selectTimeDomineLab.place(x = 40, y= 195)



btnShowF1F2Graphs = Button(main, text = 'Graph functions', command = GraphF1)
btnShowF1F2Graphs.config(bg='gainsboro')
btnShowF1F2Graphs.place(x = 345, y = 195)

traslapedFuntionsLabel = Label(main, text = 'Traslaped functions')
traslapedFuntionsLabel.configure(pady = 5, padx = 1, bg = 'gainsboro')
traslapedFuntionsLabel.place(x = 260, y= 360)
main.mainloop()




