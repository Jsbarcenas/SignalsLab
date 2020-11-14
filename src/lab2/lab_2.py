##Bueno profe, aquí hoy, martes 22  a las 5:05 de la tarde comienzo con su laboratorio.
##Espero disfrute leyendo este código. ;) f

import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from scipy import signal as sp
from tkinter import ttk
import scipy.stats as sp 








main = Tk()
main.config(bg = 'gainsboro')
main.geometry('1200x540')
main.resizable(0,0)
main.title('Signal Convolutions')
titleLabel= Label(main, text = 'Laboratory 2th-- Signal Convolutions')
titleLabel.config( padx = 5, pady= 5, bg = 'gainsboro')
titleLabel.place(x = 500)

titleLabelConv = Label( main, text = ' Conv Functions')
titleLabelConv.config( padx = 5, pady= 5, bg = 'gainsboro')
titleLabelConv.place(x = 900, y = 50)



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

timeGeneratorF1 = 1
timeGeneratorF2 = 1
plotF1GeneratorStatus = [1]
plotF1TimeGeneratorStatus= [1]

plotF2GeneratorStatus = [1]
plotF2TimeGeneratorStatus= [1]

periodDef2=1

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

    amplitudF1Entry = Entry(function1, state = 'normal')
    amplitudF1Entry.config(bd = 2, width= 5)
    amplitudF1Entry.place( x = 60, y = 65)
    periodF1Entry = Entry(function1, state = 'normal')
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
def GraphF1():
    global timeGeneratorF1
    global plotF1GeneratorStatus
    global plotF1TimeGeneratorStatus
    global periodDef
    global timeGeneratorF1Else
    print(timeDomineStatus)
    if timeDomineStatus == 1:
        ts = 0.01
    if timeDomineStatus == 0:
        ts = 0.125  
    if selectF1Lab.get() == 'Exponential':
        timeGeneratorExponetial = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        exponentialGenerator = np.exp(timeGeneratorExponetial*float(exponentF1Entry.get()))*float(amplitudF1Entry.get())
        plotF1TimeGeneratorStatus =  timeGeneratorExponetial
        plotF1GeneratorStatus = exponentialGenerator
        canvasChange()
        print(exponentialGenerator)
    if selectF1Lab.get() == 'Sinusoidal':
        periodDef =float(periodF1Entry.get())
        print(periodDef)
        timeGeneratorF1Else = np.arange(0,periodDef,ts)
        sinusoidalGenerator = (np.sin(2*np.pi*(timeGeneratorF1Else)))*float(amplitudF1Entry.get())
        plotF1TimeGeneratorStatus = timeGeneratorF1Else
        plotF1GeneratorStatus = sinusoidalGenerator
        canvasChange()
        print(sinusoidalGenerator)
    if selectF1Lab.get() == 'Triangular':
        periodDef =float(periodF1Entry.get())
        print(periodDef)
        timeGeneratorF1Else = np.arange(0,periodDef*6.3,ts)
        triangularGenerator = (sp.sawtooth(timeGeneratorF1Else))*float(amplitudF1Entry.get())
        plotF1TimeGeneratorStatus = timeGeneratorF1Else
        plotF1GeneratorStatus = triangularGenerator
        canvasChange()
        print(triangularGenerator)
    if selectF1Lab.get() == 'Rectangular':
        periodDef =float(periodF1Entry.get())
        timeGeneratorF1Else = np.arange(-0.1,6.2*periodDef,ts)
        rectangularGenerator = sp.square( timeGeneratorF1Else)
        plotF1TimeGeneratorStatus = timeGeneratorF1Else
        plotF1GeneratorStatus = rectangularGenerator
        canvasChange()
        print(exponentialGenerator)   
    if selectF1Lab.get() == 'Ramp1':
        ti = float(timeInitF1Entry.get())
        tf = float(timeFinalF1Entry.get())
        tk = tf - ti
        t = np.arange(ti,tf,ts)
        def u(t): 
            return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
        def f(t):
            return  (t-(tk/3 + (ti)))*(u(t-(tk/3+(ti)))-u(t-(tk*2/3 + (ti))))+(tk/3)*u(t-(tk*2/3 + (ti)))
        plotF1TimeGeneratorStatus = t
        plotF1GeneratorStatus = f(t)
        canvasChange()
        print(t)
    if selectF1Lab.get() == 'Ramp2':
        ti = float(timeInitF1Entry.get())
        tf = float(timeFinalF1Entry.get())
        tk = tf -ti
        t = np.arange(ti,tf,ts)
        def d(t): 
            return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
        def s(t):
             return  np.flip((t-(tk/3 + (ti)))*(d(t-(tk/3+(ti)))-d(t-(tk*2/3 + (ti))))+(tk/3)*d(t-(tk*2/3 + (ti))))
        plotF1TimeGeneratorStatus = t
        plotF1GeneratorStatus = s(t)
        canvasChange()
        print(t)
    if selectF1Lab.get() == 'Ramp3':
        ti = float(timeInitF1Entry.get())
        tf = float(timeFinalF1Entry.get())
        tk = tf -ti 
        t = np.arange(ti,tf,ts)
        def l(t): 
            return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
        def n(t): 
            return  (t-((ti)))*(l(t-(ti))-l(t-((tk/4 ) + (ti))))+(tk/4)*l(t-(tk/4 + ti)) - ((t-((tf)-(tk/4)))*(l(t-((tf)-(tk/4)))-l(t-(tf)))-(tk)*l(t-(tf)))
        plotF1TimeGeneratorStatus = t
        plotF1GeneratorStatus = n(t)
        canvasChange()
        print(t)                                 
    if selectF1Lab.get() == 'Sustentation1':
        t = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        tf = float(timeFinalF1Entry.get())
        ti =float(timeInitF1Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = pieces
        plotF1TimeGeneratorStatus =  t
        plotF1GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)
    if selectF1Lab.get() == 'Sustentation2':
        t = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        tf = float(timeFinalF1Entry.get())
        ti =float(timeInitF1Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = np.flip(pieces)
        plotF1TimeGeneratorStatus =  t
        plotF1GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)

selectF1Lab = ttk.Combobox(function1, values = ["Exponential", "Sinusoidal", "Triangular",'Rectangular','Ramp1','Ramp2','Ramp3','Sustentation1','Sustentation2'],state="readonly")
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
    amplitudF2Entry = Entry(function2, state = 'normal')
    amplitudF2Entry.config(bd = 2, width= 5)
    amplitudF2Entry.place( x = 60, y = 65)
    periodF2Entry = Entry(function2, state = 'normal')
    periodF2Entry.config(bg = 'white',bd = 2, width= 5)
    periodF2Entry.place( x = 60, y = 95)
    exponentF2Entry = Entry(function2, state = 'normal')
    exponentF2Entry.config(bg = 'white',bd = 2, width= 5)
    exponentF2Entry.place( x = 160, y = 65)
    timeInitF2Entry = Entry(function2, state ='normal')
    timeInitF2Entry.config(bg = 'white',bd = 2, width= 5)
    timeInitF2Entry.place( x = 160, y = 95)
    timeFinalF2Entry = Entry(function2, state = 'normal')
    timeFinalF2Entry.config(bg = 'white',bd = 2, width= 5)
    timeFinalF2Entry.place( x = 260, y = 95)

def GraphF2():
    global plotF2GeneratorStatus
    global plotF2TimeGeneratorStatus
    global periodDef2
    global timeGeneratorF2Else
    print(timeDomineStatus)
    if timeDomineStatus == 0:
        ts2 =0.125
    if timeDomineStatus == 1:
        ts2 = 0.01
    if selectF2Lab.get() == 'Exponential':
        timeGeneratorExponetial = np.arange(float(timeInitF2Entry.get()),float(timeFinalF2Entry.get()),ts2)
        exponentialGenerator = np.exp(timeGeneratorExponetial*float(exponentF2Entry.get()))*float(amplitudF2Entry.get())
        plotF2TimeGeneratorStatus =  timeGeneratorExponetial
        plotF2GeneratorStatus = exponentialGenerator
        canvasChange()
        print(exponentialGenerator)
    if selectF2Lab.get() == 'Sinusoidal':
        periodDef2 =float(periodF2Entry.get())
        print(periodDef2)
        timeGeneratorF2Else = np.arange(0,periodDef2,ts2)
        sinusoidalGenerator = (np.sin(2*np.pi*(timeGeneratorF2Else)))*float(amplitudF2Entry.get())
        plotF2TimeGeneratorStatus = timeGeneratorF2Else
        plotF2GeneratorStatus = sinusoidalGenerator
        canvasChange()
        print(sinusoidalGenerator)
    if selectF2Lab.get() == 'Triangular':
        periodDef2 =float(periodF2Entry.get())
        print(periodDef2)
        timeGeneratorF2Else = np.arange(0,periodDef2*6.3,ts2)
        triangularGenerator = (sp.sawtooth(timeGeneratorF2Else))*float(amplitudF2Entry.get())
        plotF2TimeGeneratorStatus = timeGeneratorF2Else
        plotF2GeneratorStatus = triangularGenerator
        canvasChange()
        print(triangularGenerator)
    if selectF2Lab.get() == 'Rectangular':
        periodDef2 =float(periodF2Entry.get())
        timeGeneratorF2Else = np.arange(-0.1,6.2*periodDef2,ts2)
        rectangularGenerator = sp.square( timeGeneratorF2Else)
        plotF2TimeGeneratorStatus = timeGeneratorF2Else
        plotF2GeneratorStatus = rectangularGenerator
        canvasChange()
        print(exponentialGenerator)   
    if selectF2Lab.get() == 'Ramp1':
        ti = float(timeInitF2Entry.get())
        tf = float(timeFinalF2Entry.get())
        tk = tf - ti
        t = np.arange(ti,tf,ts2)
        def u(t): 
            return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
        def f(t):
            return  (t-(tk/3 + (ti)))*(u(t-(tk/3+(ti)))-u(t-(tk*2/3 + (ti))))+(tk/3)*u(t-(tk*2/3 + (ti)))
        plotF2TimeGeneratorStatus = t
        plotF2GeneratorStatus = f(t)
        canvasChange()
        print(f(t))
    if selectF2Lab.get() == 'Ramp2':
        ti = float(timeInitF2Entry.get())
        tf = float(timeFinalF2Entry.get())
        tk = tf - ti
        t = np.arange(ti,tf,ts2)
        def d(t): 
            return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
        def s(t):
             return  np.flip((t-(tk/3 + (ti)))*(d(t-(tk/3+(ti)))-d(t-(tk*2/3 + (ti))))+(tk/3)*d(t-(tk*2/3 + (ti))))
        plotF2TimeGeneratorStatus = t
        plotF2GeneratorStatus = s(t)
        canvasChange()
        print(s(t))
    if selectF2Lab.get() == 'Ramp3':
        ti = float(timeInitF2Entry.get())
        tf = float(timeFinalF2Entry.get())
        tk = tf - ti
        t = np.arange(ti,tf,ts2)
        def l(t): 
            return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
        def n(t): 
            return  (t-((ti)))*(l(t-(ti))-l(t-((tk/4 ) + (ti))))+(tk/4)*l(t-(tk/4 + ti)) - ((t-((tf)-(tk/4)))*(l(t-((tf)-(tk/4)))-l(t-(tf)))-(tk)*l(t-(tf)))
        plotF2TimeGeneratorStatus = t
        plotF2GeneratorStatus = n(t)
        canvasChange()
        print(n(t))                                     
    if selectF2Lab.get() == 'Sustentation1':
        t = np.arange(float(timeInitF2Entry.get()),float(timeFinalF2Entry.get()),ts2)
        tf = float(timeFinalF2Entry.get())
        ti =float(timeInitF2Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = pieces
        plotF2TimeGeneratorStatus =  t
        plotF2GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)
    if selectF2Lab.get() == 'Sustentation2':
        t = np.arange(float(timeInitF2Entry.get()),float(timeFinalF2Entry.get()),ts2)
        tf = float(timeFinalF2Entry.get())
        ti =float(timeInitF2Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = np.flip(pieces)
        plotF2TimeGeneratorStatus =  t
        plotF2GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)

       
selectF2Lab = ttk.Combobox(function2, values = ["Exponential", "Sinusoidal", "Triangular",'Rectangular','Ramp1','Ramp2','Ramp3','Sustentation1','Sustentation2'],state="readonly")
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
    global plotF2GeneratorStatus
    global plotF2TimeGeneratorStatus
    global figF1
    global figF2
    global figF3
    global canv
    global figuresNumber1 
    global figuresNumber2
    global figuresNumber3

    
        
    if timeDomineStatus == 0:
        plt.figure(1)
        plt.clf()
        plt.plot(plotF1TimeGeneratorStatus, plotF1GeneratorStatus, marker =  'o', linewidth=0)
        plt.gcf().canvas.draw()
 
        plt.figure(2)
        plt.clf()
        plt.plot(plotF2TimeGeneratorStatus,plotF2GeneratorStatus, marker =  'o', linewidth=0, color = 'black')
        plt.gcf().canvas.draw()

        plt.figure(3)
        plt.clf()
        plt.plot(plotF1TimeGeneratorStatus, plotF1GeneratorStatus, marker =  'o', linewidth=0)
        plt.plot(plotF2TimeGeneratorStatus,np.flip(plotF2GeneratorStatus), marker =  'o', linewidth=0, color = 'black')
        plt.gcf().canvas.draw()
    if timeDomineStatus == 1:
        plt.figure(1)
        plt.clf()
        plt.plot(plotF1TimeGeneratorStatus, plotF1GeneratorStatus)
        plt.gcf().canvas.draw()
 
        plt.figure(2)
        plt.clf()
        plt.plot(plotF2TimeGeneratorStatus,plotF2GeneratorStatus, color = 'black')
        plt.gcf().canvas.draw()

        plt.figure(3)
        plt.clf()
        plt.plot(plotF1TimeGeneratorStatus, plotF1GeneratorStatus)
        plt.plot(plotF2TimeGeneratorStatus,np.flip(plotF2GeneratorStatus), color = 'black')
        plt.gcf().canvas.draw()
        
        
      


        
       
    
def showConv():
    global plotF1GeneratorStatus
    global plotF1TimeGeneratorStatus
    global plotF2GeneratorStatus
    global plotF2TimeGeneratorStatus

    if timeDomineStatus == 1:
    
        convGenerator = np.convolve(plotF1GeneratorStatus,plotF2GeneratorStatus)
        ti = min(plotF1TimeGeneratorStatus) + min(plotF2TimeGeneratorStatus)
        tf= max(plotF1TimeGeneratorStatus) + max(plotF2TimeGeneratorStatus)
        ds = 0.01
        convTimeGenerator = np.linspace(ti,tf,len(convGenerator))

        plt.figure(4)
        plt.clf()
        plt.plot(convTimeGenerator , convGenerator )
        plt.gcf().canvas.draw()
    if timeDomineStatus == 0:

        convGenerator = np.convolve(plotF1GeneratorStatus,plotF2GeneratorStatus)
        ti = min(plotF1TimeGeneratorStatus) + min(plotF2TimeGeneratorStatus)
        tf= max(plotF1TimeGeneratorStatus) + max(plotF2TimeGeneratorStatus)
        ds = 0.125
        convTimeGenerator = np.linspace(ti,tf,len(convGenerator))

        plt.figure(4)
        plt.clf()
        plt.stem(convTimeGenerator , convGenerator)
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

figF4 = plt.figure(figsize=(9, 2), facecolor ="gainsboro", dpi = 72)
canv = FigureCanvasTkAgg(figF4, master=main)
canv.get_tk_widget().place(x = 600, y= 90)
plt.clf()
plt.figure(4)
plt.plot(2,2)
plt.gcf().canvas.draw()

selecTimeDomineComb = ttk.Combobox(main, values = ['Continuous','Discrete'],state="readonly")
selecTimeDomineComb.place(x = 150, y= 195)
selecTimeDomineComb.current(0)
selecTimeDomineComb.bind("<<ComboboxSelected>>", changeTimeDomine)

selectTimeDomineLab = Label(main, text = 'Select Time Domine')
selectTimeDomineLab.configure(bg= 'gainsboro')
selectTimeDomineLab.place(x = 40, y= 195)

def commandAcept1 ():
    GraphF2()
    GraphF1()
    
btnShowF1F2Graphs = Button(main, text = 'Graph functions', command = commandAcept1)
btnShowF1F2Graphs.config(bg='gainsboro')
btnShowF1F2Graphs.place(x = 345, y = 195)

bntShowConv = Button(main, text = 'Show Conv', command = showConv)
bntShowConv.config(bg='gainsboro')
bntShowConv.place(x = 680, y = 75)

traslapedFuntionsLabel = Label(main, text = 'Traslaped functions')
traslapedFuntionsLabel.configure(pady = 5, padx = 1, bg = 'gainsboro')
traslapedFuntionsLabel.place(x = 260, y= 360)
main.mainloop()





