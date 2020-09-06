
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

        
        labFrecuency = Label(triWin, text="Signal Frecuency")
        labFrecuency.configure(background='white')
        labFrecuency.grid(row=5, column=1, padx=(1, 1), pady=(5, 5))
        frecuency = Entry(triWin)
        frecuency.configure(background='white', bd=2, relief='sunken')
        frecuency.grid(row=5, column=2, padx=(1, 1), pady=(5, 5))
        frecuency.config(width=10)

        triValueTLab = Label(triWin, text = 'Operations Values')
        triValueTLab.configure(bg= 'gray')
        triValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))

        triScalationTLab = Label(triWin, text = 'Scalation(t)')
        triScalationTLab.configure(bg= 'white')
        triScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        triScalationTEntry = Entry(triWin)
        triScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        triScalationALab = Label(triWin, text = 'Scalation(A)')
        triScalationALab.configure(bg= 'white')
        triScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        triScalationAEntry = Entry(triWin)
        triScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        triDesplacementTLab = Label(triWin, text = 'Desplacement(t)')
        triDesplacementTLab.configure(bg= 'white')
        triDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        triDesplacementTEntry = Entry(triWin)
        triDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

       
        def showGraph():
            if triScalationAEntry.get() == '':
                triScalationAValue = 1
            else :
                triScalationAValue = float(triScalationAEntry.get())
            if triScalationTEntry.get() ==  '':
                triScalationTValue= 1
            else:
                triScalationTValue= float(triScalationTEntry.get())
            if triDesplacementTEntry.get() == '':
                triDesplacementTValue = 0
            else:
                triDesplacementTValue = float(triDesplacementTEntry.get())
            
            a = amplitud.get()
            if a == '':
                a = 1
            else :
                a = float(a)
                
            if frecuency.get() == '':
                f = 1
            else:
                f = float(frecuency.get())   

            Ts = f*100
            
            ti = float(t_ini.get())
            tf = float(t_fin.get())

            t = np.arange(ti, tf, 1/Ts)
            y = a*np.sin(2*np.pi*t*f)
           

            if triScalationAEntry.get() or triScalationTEntry.get() or  triDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,6))
                plt.subplot(2,2,1)
                plt.plot(t,y  )
                plt.title('Original Signal')
                plt.subplot(2,2,3)
                plt.plot(1/triScalationTValue*(t-triDesplacementTValue), triScalationAValue*y , color = 'orange')
                plt.title('Transformated Signal')
                plt.show()
            else:
                
                plt.figure(figsize = (9,11))
                plt.plot((t),y )
                plt.show()
            
            

        btn = Button(triWin, text="Mostrar Gráfica", command=showGraph)
        btn.grid(row=6, column=1, padx=(1, 1), pady=(10, 10))
        btn.config(cursor='hand2', bd='5', relief='groove')

        
        triWin.mainloop()
    if choose.get() == 'Pulse':
        pulseWin = Tk()
        pulseWin.title("Pulse Signal")
        pulseWin.geometry('800x600')
        pulseWin.resizable(0,0)
        pulseWin.config(bg= 'white', padx = 50, pady= 50)

        pulseTimeInitLab = Label(pulseWin, text = 'Time init')
        pulseTimeInitLab.configure(bg= 'white')
        pulseTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        pulseTimeInitEntry = Entry(pulseWin)
        pulseTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        pulseTimeFinalLab = Label(pulseWin, text = 'Time final')
        pulseTimeFinalLab.configure(bg= 'white')
        pulseTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        pulseTimeFinalEntry = Entry(pulseWin)
        pulseTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        pulseSamplingLab = Label(pulseWin, text = 'Sampling step')
        pulseSamplingLab.configure(bg= 'white')
        pulseSamplingLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        pulseSamplingEntry = Entry(pulseWin)
        pulseSamplingEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseSamplingEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))
        
        pulseAmplitudLab = Label(pulseWin, text = 'Amplitud')
        pulseAmplitudLab.configure(bg= 'white')
        pulseAmplitudLab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        pulseAmplitudEntry = Entry(pulseWin)
        pulseAmplitudEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseAmplitudEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        pulseLenghtLab = Label(pulseWin, text = 'Lenght')
        pulseLenghtLab.configure(bg= 'white')
        pulseLenghtLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        pulseLenghtEntry = Entry(pulseWin)
        pulseLenghtEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseLenghtEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))

        pulseInitTime = Label(pulseWin, text = 'Pulse Init Time')
        pulseInitTime.configure(bg= 'white')
        pulseInitTime.grid(row = 6, column = 1, padx = (1,1), pady= (5,5))
        pulseInitTimeEntry = Entry(pulseWin)
        pulseInitTimeEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseInitTimeEntry.grid(row= 6 ,column= 2, padx=(1,1), pady= (5,5))

        pulseValueTLab = Label(pulseWin, text = 'Operations Values')
        pulseValueTLab.configure(bg= 'gray')
        pulseValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))

        pulseScalationTLab = Label(pulseWin, text = 'Scalation(t)')
        pulseScalationTLab.configure(bg= 'white')
        pulseScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        pulseScalationTEntry = Entry(pulseWin)
        pulseScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        pulseScalationALab = Label(pulseWin, text = 'Scalation(A)')
        pulseScalationALab.configure(bg= 'white')
        pulseScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        pulseScalationAEntry = Entry(pulseWin)
        pulseScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        pulseDesplacementTLab = Label(pulseWin, text = 'Desplacement(t)')
        pulseDesplacementTLab.configure(bg= 'white')
        pulseDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        pulseDesplacementTEntry = Entry(pulseWin)
        pulseDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        pulseDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        
        
        def pulseShowGraph():
            if pulseScalationAEntry.get() == '':
                pulseScalationAValue = 1
            else :
                pulseScalationAValue = float(pulseScalationAEntry.get())
            if pulseScalationTEntry.get() ==  '':
                pulseScalationTValue= 1
            else:
                pulseScalationTValue= float(pulseScalationTEntry.get())
            if pulseDesplacementTEntry.get() == '':
                pulseDesplacementTValue = 0
            else:
                pulseDesplacementTValue = float(pulseDesplacementTEntry.get())
            pulseInitTimeValue = float(pulseInitTimeEntry.get())
            amplitudValue = float(pulseAmplitudEntry.get())
            lenghtValue = float(pulseLenghtEntry.get())
            pulseStepValue = float(pulseSamplingEntry.get())
            pulseTimeInitValue = float(pulseTimeInitEntry.get())
            pulseTimeFinalValue = float(pulseTimeFinalEntry.get())
            
            pulseTime = np.arange(pulseTimeInitValue,pulseTimeFinalValue,1/pulseStepValue)
            pulsePart1 = np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue,[1*amplitudValue,0])

            pulsePart2 = np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue+lenghtValue,[1*amplitudValue,0])
            
            pulsePart3 =np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue+lenghtValue*2,[1*amplitudValue,0])
            pulsePart4 = np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue+lenghtValue*3,[1*amplitudValue,0])
            pulsePart5= np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue+lenghtValue*4,[1*amplitudValue,0])
            pulsePart6= np.piecewise(pulseTime,pulseTime>=pulseInitTimeValue+lenghtValue*5,[1*amplitudValue,0])
            pulseGenerate = pulsePart1 - pulsePart2 + (pulsePart3-pulsePart4) + (pulsePart5- pulsePart6)

            if pulseScalationAEntry.get() or pulseScalationTEntry.get() or  pulseDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,6))
                plt.subplot(2,2,1)
                plt.plot(pulseTime,pulseGenerate  )
                plt.title('Original Signal')
                plt.subplot(2,2,3)
                plt.plot(1/pulseScalationTValue*(pulseTime-pulseDesplacementTValue), pulseScalationAValue*pulseGenerate , color = 'orange')
                plt.title('Transformated Signal')
                plt.show()
            else:
                
                plt.figure(figsize = (9,11))
                plt.plot((pulseTime),pulseGenerate )
                plt.show()

           
          

            

        pulseShowGraphBtn = Button(pulseWin, text="Show Graph", command = pulseShowGraph)
        pulseShowGraphBtn.grid(row=7, column=1, padx=(1, 1), pady=(10, 10))
        pulseShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        

    if choose.get() == 'Quadratic' :
        quadraticWin = Tk()
        quadraticWin.title('Quadratic Signal')
        quadraticWin.geometry('800x600')
        quadraticWin.resizable(0,0)
        quadraticWin.config(bg= 'white', padx = 50, pady= 50)

        quadraticTimeInitLab = Label(quadraticWin, text = 'Time Init')
        quadraticTimeInitLab.configure(bg= 'white')
        quadraticTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        quadraticTimeInitEntry = Entry(quadraticWin)
        quadraticTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        quadraticTimeFinalLab = Label(quadraticWin, text = 'Time Final')
        quadraticTimeFinalLab.configure(bg= 'white')
        quadraticTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        quadraticTimeFinalEntry = Entry(quadraticWin)
        quadraticTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        quadraticTimeSamplingLab = Label(quadraticWin, text = 'Time sampling')
        quadraticTimeSamplingLab.configure(bg= 'white')
        quadraticTimeSamplingLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        quadraticTimeSamplingEntry = Entry(quadraticWin)
        quadraticTimeSamplingEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticTimeSamplingEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))

        quadraticConstALab = Label(quadraticWin, text = 'Const a (a*t^2)')
        quadraticConstALab.configure(bg= 'white')
        quadraticConstALab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        quadraticConstAEntry = Entry(quadraticWin)
        quadraticConstAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticConstAEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        quadraticConstBLab = Label(quadraticWin, text = 'Const b (b*t)')
        quadraticConstBLab.configure(bg= 'white')
        quadraticConstBLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        quadraticConstBEntry = Entry(quadraticWin)
        quadraticConstBEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticConstBEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))

        quadraticConstCLab = Label(quadraticWin, text = 'Const c (c)')
        quadraticConstCLab.configure(bg= 'white')
        quadraticConstCLab.grid(row = 6, column = 1, padx = (1,1), pady= (5,5))
        quadraticConstCEntry = Entry(quadraticWin)
        quadraticConstCEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticConstCEntry.grid(row= 6 ,column= 2, padx=(1,1), pady= (5,5))

        quadraticValueTLab = Label(quadraticWin, text = 'Operations Values')
        quadraticValueTLab.configure(bg= 'gray')
        quadraticValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))

        quadraticScalationTLab = Label(quadraticWin, text = 'Scalation(t)')
        quadraticScalationTLab.configure(bg= 'white')
        quadraticScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        quadraticScalationTEntry = Entry(quadraticWin)
        quadraticScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        quadraticScalationALab = Label(quadraticWin, text = 'Scalation(A)')
        quadraticScalationALab.configure(bg= 'white')
        quadraticScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        quadraticScalationAEntry = Entry(quadraticWin)
        quadraticScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        quadraticDesplacementTLab = Label(quadraticWin, text = 'Desplacement(t)')
        quadraticDesplacementTLab.configure(bg= 'white')
        quadraticDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        quadraticDesplacementTEntry = Entry(quadraticWin)
        quadraticDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        quadraticDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

            


        def quadraticShowGraph():
        
            if quadraticScalationAEntry.get() == '':
                quadraticScalationAValue = 1
            else :
                quadraticScalationAValue = float(quadraticScalationAEntry.get())
            if quadraticScalationTEntry.get() ==  '':
                quadraticScalationTValue= 1
            else:
                quadraticScalationTValue= float(quadraticScalationTEntry.get())
            if quadraticDesplacementTEntry.get() == '':
                quadraticDesplacementTValue = 0
            else:
                quadraticDesplacementTValue = float(quadraticDesplacementTEntry.get())

            quadraticTimeInitValue = float(quadraticTimeInitEntry.get())
            quadraticTimeSamplingValue = float(quadraticTimeSamplingEntry.get())
            quadraticTimeFinalValue = float(quadraticTimeFinalEntry.get())
            quadraticConstAValue = float(quadraticConstAEntry.get())
            quadraticConstBValue = float(quadraticConstBEntry.get())
            quadraticConstCValue = float(quadraticConstCEntry.get())
            quadraticTime = np.arange(quadraticTimeInitValue, quadraticTimeFinalValue, 1/quadraticTimeSamplingValue)
            quadraticGenerator= quadraticConstAValue*(quadraticTime**2)+ quadraticConstBValue*(quadraticTime)+ quadraticConstCValue
            if quadraticScalationAEntry.get() or quadraticScalationTEntry.get() or  quadraticDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,6))
                plt.subplot(2,2,1)
                plt.plot((quadraticTime),quadraticGenerator )
                plt.title('Original Signal')
                plt.subplot(2,2,3)
                plt.plot(1/quadraticScalationTValue*(quadraticTime-quadraticDesplacementTValue), quadraticScalationAValue*quadraticGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.show()
            else:
                
                
                plt.plot((quadraticTime),quadraticGenerator )
                plt.show()
                
            
            
            
            plt.show()

        

        

        quadraticShowGraphBtn = Button(quadraticWin, text="Show Graph", command = quadraticShowGraph)
        quadraticShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        quadraticShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')
        

        quadraticWin.mainloop()


        







chooseSignalBtn= Button(main, text = 'Acept', command= showGraphicWindows )
chooseSignalBtn.configure(cursor = 'hand2',bg= 'white', bd = 3)
chooseSignalBtn.grid(sticky = 'w',row = 3, column = 1, padx = (2,2), pady= (10,10))






main.mainloop()




