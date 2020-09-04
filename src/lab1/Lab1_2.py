
import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from scipy import signal as sp

main = Tk()
main.title('Signal Selection')
main.geometry('300x270')
main.configure(bg='white',padx= 50, pady= 50)
main.resizable(0,0)
txt1 = Label(main, text = 'Pleas select a signal to Graph.')
txt1.configure(bg = 'white')
txt1.grid(row=1, column =1)

choose = StringVar()
choose.set('Select Signal')
chooseSignalToggle = OptionMenu(main, choose, 'Select Signal', 'Trigonometric', 'Pulse', 'Quadratic','Exponential', 'Lineal', 'UnitSetp', 'Delta','Triangular','Square')
chooseSignalToggle.grid(sticky = 'W',row= 2, column = 1,padx=(2, 2), pady=(10, 10))
chooseSignalToggle.configure(bg= 'white', cursor = 'hand2')


def showGraphicWindows():
    if choose.get() == 'Trigonometric':
        ##Aquí me tomé la libertad tomar código de sus ejemplos
        ##NO es porque no pudiera hacerlo yo mismo, sino porque
        ##Necesito ahorrar tiempo. 
        triWin = Tk ()
        triWin.title('Sin(t) Singal')
        triWin.configure(bg= 'white', padx= 50, pady= 50)
        triWin.geometry('600x400')

        lab_ini = Label(triWin, text="Initial Time")
        lab_ini.configure(background='white')
        lab_ini.grid(row=1, column=1, padx=(1, 1), pady=(5, 5))
        t_ini = Entry(triWin)
        t_ini.configure(background='white', bd=2, relief='sunken')
        t_ini.grid(row=1, column=2, padx=(1, 1), pady=(5, 5))
        t_ini.config(width=10)

        lab_fin = Label(triWin, text="Final Time")
        lab_fin.configure(background='white')
        lab_fin.grid(row=2, column=1, padx=(1, 1), pady=(5, 5))
        t_fin = Entry(triWin)
        t_fin.configure(background='white', bd=2, relief='sunken')
        t_fin.grid(row=2, column=2, padx=(1, 1), pady=(5, 5))
        t_fin.config(width=10)

        lab_ts = Label(triWin, text="Sampling Step")
        lab_ts.configure(background='white')
        lab_ts.grid(row=3, column=1, padx=(1, 1), pady=(5, 5))
        ts = Entry(triWin)
        ts.configure(background='white', bd=2, relief='sunken')
        ts.grid(row=3, column=2, padx=(1, 1), pady=(5, 5))
        ts.config(width=10)

        labAmplitud = Label(triWin, text="Amplitud")
        labAmplitud.configure(background='white')
        labAmplitud.grid(row=4, column=1, padx=(1, 1), pady=(5, 5))
        amplitud = Entry(triWin)
        amplitud.configure(background='white', bd=2, relief='sunken')
        amplitud.grid(row=4, column=2, padx=(1, 1), pady=(5, 5))
        amplitud.config(width=10)

       
        def showGraph():
            a = amplitud.get()
            if a == '':
                a = 1
            else :
                a = float(a)
            ti = float(t_ini.get())
            tf = float(t_fin.get())
            Ts = float(ts.get())
            t = np.arange(ti, tf, Ts)
            y = a*np.sin(2*np.pi*t)
            plt.figure(1)
            plt.clf()
            plt.title('Señal')
            plt.plot(t, y)
            plt.gcf().canvas.draw()

        btn = Button(triWin, text="Mostrar Gráfica", command=showGraph)
        btn.grid(row=5, column=1, padx=(1, 1), pady=(10, 10))
        btn.config(cursor='hand2', bd='5', relief='groove')

        fig = plt.figure(figsize=(3, 2))
        canv = FigureCanvasTkAgg(fig, master=triWin)
        canv.get_tk_widget().grid(row=5, column=2, padx=(1, 1), pady=(10, 10))
        triWin.mainloop()
    if choose.get() == 'Pulse':
        pusleWin = Tk()
        pusleWin.geometry('800x600')
        pusleWin.resizable(0,0)
        pusleWin.config(bg= 'white', padx = 50, pady= 50)

        pulseTimeInitLab = Label(pusleWin, text = 'Time init')
        pulseTimeInitLab.configure(bg= 'white')
        pulseTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        pulseTimeInitEntry = Entry(pusleWin)
        pulseTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        pulseTimeFinalLab = Label(pusleWin, text = 'Time final')
        pulseTimeFinalLab.configure(bg= 'white')
        pulseTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        pulseTimeFinalEntry = Entry(pusleWin)
        pulseTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        pulseSamplingLab = Label(pusleWin, text = 'Sampling step')
        pulseSamplingLab.configure(bg= 'white')
        pulseSamplingLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        pulseSamplingEntry = Entry(pusleWin)
        pulseSamplingEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseSamplingEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))
        
        pulseAmplitudLab = Label(pusleWin, text = 'Amplitud')
        pulseAmplitudLab.configure(bg= 'white')
        pulseAmplitudLab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        pulseAmplitudEntry = Entry(pusleWin)
        pulseAmplitudEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseAmplitudEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        pulseLenghtLab = Label(pusleWin, text = 'Lenght (0.1-0.9)')
        pulseLenghtLab.configure(bg= 'white')
        pulseLenghtLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        pulseLenghtEntry = Entry(pusleWin)
        pulseLenghtEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseLenghtEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))

        pulseInitTime = Label(pusleWin, text = 'Pulse Init Time')
        pulseInitTime.configure(bg= 'white')
        pulseInitTime.grid(row = 6, column = 1, padx = (1,1), pady= (5,5))
        pulseInitTimeEntry = Entry(pusleWin)
        pulseInitTimeEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseInitTimeEntry.grid(row= 6 ,column= 2, padx=(1,1), pady= (5,5))

        
        
        def pulseShowGraph():
            pulseInitTimeValue = float(pulseInitTimeEntry.get())
            amplitudValue = float(pulseAmplitudEntry.get())
            lenghtValue = float(pulseLenghtEntry.get())
            pulseStepValue = float(pulseSamplingEntry.get())
            pulseTimeInitValue = float(pulseTimeInitEntry.get())
            pulseTimeFinalValue = float(pulseTimeFinalEntry.get())
            
            pulseTime = np.arange(pulseTimeInitValue,pulseTimeFinalValue,pulseStepValue)
            pulsePart1 = np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue,[1*amplitudValue,0])

            pulsePart2 = np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue+lenghtValue,[1*amplitudValue,0])
            pulseGenerate = pulsePart1 - pulsePart2 
            plt.figure(1)
            plt.clf()
            plt.title('Signal')
            plt.plot(pulseTime, pulseGenerate)
            plt.gcf().canvas.draw()

            

        pulseShowGraphBtn = Button(pusleWin, text="Show Graph", command = pulseShowGraph)
        pulseShowGraphBtn.grid(row=7, column=1, padx=(1, 1), pady=(10, 10))
        pulseShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        pulseFigure= plt.figure(figsize=(8, 2))
        pulseCanvas = FigureCanvasTkAgg(pulseFigure, master=pusleWin)
        pulseCanvas.get_tk_widget().grid(row=7, column=2, padx=(1, 1), pady=(10, 10))



        pusleWin.mainloop()


        







chooseSignalBtn= Button(main, text = 'Acept', command= showGraphicWindows )
chooseSignalBtn.configure(cursor = 'hand2',bg= 'white', bd = 3)
chooseSignalBtn.grid(sticky = 'w',row = 3, column = 1, padx = (2,2), pady= (10,10))






main.mainloop()




