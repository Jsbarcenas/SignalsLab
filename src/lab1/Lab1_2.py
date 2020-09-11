
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
chooseSignalToggle = OptionMenu(main, choose, 'Select Signal', 'Trigonometric', 'Pulse', 'Quadratic','Exponential', 'Lineal', 'UnitSetp', 'Delta','Triangular','Square', 'sust1','sust2')
chooseSignalToggle.grid(sticky = 'W',row= 2, column = 1,padx=(2, 2), pady=(10, 10))
chooseSignalToggle.configure(bg= 'white', cursor = 'hand2')



def showGraphicWindows():
    if choose.get() == 'Trigonometric':
        #Aquí me tomé la libertad tomar código de sus ejemplos
        #NO es porque no pudiera hacerlo yo mismo, sino porque
        #Necesito ahorrar tiempo. 
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
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot(t,y  )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/triScalationTValue*(t-triDesplacementTValue), triScalationAValue*y , color = 'orange')
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot(t,y  )
                plt.plot(1/triScalationTValue*(t-triDesplacementTValue), triScalationAValue*y , color = 'orange')
                plt.xlabel('t(s)')
                plt.title('Overlapping signals')

                plt.show()
            else:
                
                plt.figure(figsize = (7,7))
                plt.plot((t),y )
                plt.xlabel('t(s)')
                plt.show()
            
            

        btn = Button(triWin, text="Mostrar Gráfica", command=showGraph)
        btn.grid(row=6, column=1, padx=(1, 1), pady=(10, 10))
        btn.config(cursor='hand2', bd='5', relief='groove')

        
        triWin.mainloop()
    if choose.get() == 'Pulse':
        pulseWin = Tk()
        pulseWin.title("Pulse Signal")
        pulseWin.geometry('600x400')
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
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot(pulseTime,pulseGenerate  )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/pulseScalationTValue*(pulseTime-pulseDesplacementTValue), pulseScalationAValue*pulseGenerate , color = 'orange')
                plt.title('Transformated Signal')
                plt.subplot(2,2,4)
                plt.plot(pulseTime,pulseGenerate  )
                plt.plot(1/pulseScalationTValue*(pulseTime-pulseDesplacementTValue), pulseScalationAValue*pulseGenerate , color = 'orange')
                plt.xlabel('t(s)')
                plt.title('Overlapping signals')

                plt.show()
            else:
                
                plt.figure(figsize = (7,7))
                plt.plot((pulseTime),pulseGenerate )
                plt.xlabel('t(s)')
                plt.show()

           
          

            

        pulseShowGraphBtn = Button(pulseWin, text="Show Graph", command = pulseShowGraph)
        pulseShowGraphBtn.grid(row=7, column=1, padx=(1, 1), pady=(10, 10))
        pulseShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        

    if choose.get() == 'Quadratic' :
        quadraticWin = Tk()
        quadraticWin.title('Quadratic Signal')
        quadraticWin.geometry('600x400')
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
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((quadraticTime),quadraticGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/quadraticScalationTValue*(quadraticTime-quadraticDesplacementTValue), quadraticScalationAValue*quadraticGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.subplot(2,2,4)
                plt.plot((quadraticTime),quadraticGenerator )
                plt.plot(1/quadraticScalationTValue*(quadraticTime-quadraticDesplacementTValue), quadraticScalationAValue*quadraticGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('Overlapping signals')
                plt.show()
            else:
                
                
                plt.plot((quadraticTime),quadraticGenerator )
                plt.xlabel('t(s)')
                plt.show()
                
            
            
            
            
   

        

        quadraticShowGraphBtn = Button(quadraticWin, text="Show Graph", command = quadraticShowGraph)
        quadraticShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        quadraticShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')
        

        quadraticWin.mainloop()

    
    if choose.get()== 'Exponential' :
        expoWin= Tk()
        expoWin.title('expo Signal')
        expoWin.geometry('600x400')
        expoWin.resizable(0,0)
        expoWin.config(bg= 'white', padx = 50, pady= 50)

        expoTimeInitLab = Label(expoWin, text = 'Time Init')
        expoTimeInitLab.configure(bg= 'white')
        expoTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        expoTimeInitEntry = Entry(expoWin)
        expoTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        expoTimeFinalLab = Label(expoWin, text = 'Time Final')
        expoTimeFinalLab.configure(bg= 'white')
        expoTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        expoTimeFinalEntry = Entry(expoWin)
        expoTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        expoTimeSamplingLab = Label(expoWin, text = 'Time sampling')
        expoTimeSamplingLab.configure(bg= 'white')
        expoTimeSamplingLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        expoTimeSamplingEntry = Entry(expoWin)
        expoTimeSamplingEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoTimeSamplingEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))

        expoConstALab = Label(expoWin, text = 'Const A (Ae^-bt)')
        expoConstALab.configure(bg= 'white')
        expoConstALab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        expoConstAEntry = Entry(expoWin)
        expoConstAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoConstAEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        expoConstBLab = Label(expoWin, text = 'Const b (Ae^-bt)')
        expoConstBLab.configure(bg= 'white')
        expoConstBLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        expoConstBEntry = Entry(expoWin)
        expoConstBEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoConstBEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))

        expoValueTLab = Label(expoWin, text = 'Operations Values')
        expoValueTLab.configure(bg= 'gray')
        expoValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        expoScalationTLab = Label(expoWin, text = 'Scalation(t)')
        expoScalationTLab.configure(bg= 'white')
        expoScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        expoScalationTEntry = Entry(expoWin)
        expoScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        expoScalationALab = Label(expoWin, text = 'Scalation(A)')
        expoScalationALab.configure(bg= 'white')
        expoScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        expoScalationAEntry = Entry(expoWin)
        expoScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        expoDesplacementTLab = Label(expoWin, text = 'Desplacement(t)')
        expoDesplacementTLab.configure(bg= 'white')
        expoDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        expoDesplacementTEntry = Entry(expoWin)
        expoDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        expoDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def expoShowGraph():

            if expoScalationAEntry.get() == '':
                expoScalationAValue = 1
            else :
                expoScalationAValue = float(expoScalationAEntry.get())
            if expoScalationTEntry.get() ==  '':
                expoScalationTValue= 1
            else:
                expoScalationTValue= float(expoScalationTEntry.get())
            if expoDesplacementTEntry.get() == '':
                expoDesplacementTValue = 0
            else:
                expoDesplacementTValue = float(expoDesplacementTEntry.get())

            expoTimeInitValue = float(expoTimeInitEntry.get())
            expoTimeSamplingValue = float(expoTimeSamplingEntry.get())
            expoTimeFinalValue = float(expoTimeFinalEntry.get())
            expoConstAValue = float(expoConstAEntry.get())
            expoConstBValue = float(expoConstBEntry.get())
            expoTime = np.arange(expoTimeInitValue, expoTimeFinalValue, 1/expoTimeSamplingValue)
            expoGenerator= (np.exp(-expoTime*expoConstBValue))*expoConstAValue
            if expoScalationAEntry.get() or expoScalationTEntry.get() or  expoDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((expoTime),expoGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/expoScalationTValue*(expoTime-expoDesplacementTValue), expoScalationAValue*expoGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot((expoTime),expoGenerator )
                plt.plot(1/expoScalationTValue*(expoTime-expoDesplacementTValue), expoScalationAValue*expoGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('overlapping signals')

                plt.show()
            else:
                
                
                plt.plot((expoTime),expoGenerator )
                plt.xlabel('t(s)')
                plt.show()



       


        expoShowGraphBtn = Button(expoWin, text="Show Graph", command = expoShowGraph)
        expoShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        expoShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')





        expoWin.mainloop() 


    if choose.get()== 'Lineal' :
        linWin= Tk()
        linWin.title('lineal Signal')
        linWin.geometry('600x400')
        linWin.resizable(0,0)
        linWin.config(bg= 'white', padx = 50, pady= 50)

        linTimeInitLab = Label(linWin, text = 'Time Init')
        linTimeInitLab.configure(bg= 'white')
        linTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        linTimeInitEntry = Entry(linWin)
        linTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        linTimeFinalLab = Label(linWin, text = 'Time Final')
        linTimeFinalLab.configure(bg= 'white')
        linTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        linTimeFinalEntry = Entry(linWin)
        linTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        linTimeSamplingLab = Label(linWin, text = 'Time sampling')
        linTimeSamplingLab.configure(bg= 'white')
        linTimeSamplingLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        linTimeSamplingEntry = Entry(linWin)
        linTimeSamplingEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linTimeSamplingEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))

        linConstMLab = Label(linWin, text = 'const m (mt + b).')
        linConstMLab.configure(bg= 'white')
        linConstMLab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        linConstMEntry = Entry(linWin)
        linConstMEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linConstMEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        linConstBLab = Label(linWin, text = 'Const b (mt + b)')
        linConstBLab.configure(bg= 'white')
        linConstBLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        linConstBEntry = Entry(linWin)
        linConstBEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linConstBEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))

        linValueTLab = Label(linWin, text = 'Operations Values')
        linValueTLab.configure(bg= 'gray')
        linValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        linScalationTLab = Label(linWin, text = 'Scalation(t)')
        linScalationTLab.configure(bg= 'white')
        linScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        linScalationTEntry = Entry(linWin)
        linScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        linScalationALab = Label(linWin, text = 'Scalation(A)')
        linScalationALab.configure(bg= 'white')
        linScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        linScalationAEntry = Entry(linWin)
        linScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        linDesplacementTLab = Label(linWin, text = 'Desplacement(t)')
        linDesplacementTLab.configure(bg= 'white')
        linDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        linDesplacementTEntry = Entry(linWin)
        linDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        linDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def linShowGraph():

            if linScalationAEntry.get() == '':
                linScalationAValue = 1
            else :
                linScalationAValue = float(linScalationAEntry.get())
            if linScalationTEntry.get() ==  '':
                linScalationTValue= 1
            else:
                linScalationTValue= float(linScalationTEntry.get())
            if linDesplacementTEntry.get() == '':
                linDesplacementTValue = 0
            else:
                linDesplacementTValue = float(linDesplacementTEntry.get())

            linTimeInitValue = float(linTimeInitEntry.get())
            linTimeSamplingValue = float(linTimeSamplingEntry.get())
            linTimeFinalValue = float(linTimeFinalEntry.get())
            linConstMValue = float(linConstMEntry.get())
            linConstBValue = float(linConstBEntry.get())
            linTime = np.arange(linTimeInitValue, linTimeFinalValue, 1/linTimeSamplingValue)
            linGenerator= linConstMValue*linTime + linConstBValue
            if linScalationAEntry.get() or linScalationTEntry.get() or  linDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((linTime),linGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/linScalationTValue*(linTime-linDesplacementTValue), linScalationAValue*linGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot((linTime),linGenerator )
                plt.plot(1/linScalationTValue*(linTime-linDesplacementTValue), linScalationAValue*linGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('Overlapping Signals')
                plt.show()
            else:
                
                
                plt.plot((linTime),linGenerator )
                plt.xlabel('t(s)')
                plt.show()



       


        linShowGraphBtn = Button(linWin, text="Show Graph", command = linShowGraph)
        linShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        linShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')





        linWin.mainloop()     


    if choose.get()== 'UnitSetp' :
        unitWin= Tk()
        unitWin.title(' UnitSetp Singal')
        unitWin.geometry('600x400')
        unitWin.resizable(0,0)
        unitWin.config(bg= 'white', padx = 50, pady= 50)

        unitTimeInitLab = Label(unitWin, text = 'Time Init')
        unitTimeInitLab.configure(bg= 'white')
        unitTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        unitTimeInitEntry = Entry(unitWin)
        unitTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        unitTimeFinalLab = Label(unitWin, text = 'Time Final')
        unitTimeFinalLab.configure(bg= 'white')
        unitTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        unitTimeFinalEntry = Entry(unitWin)
        unitTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        unitTimeSampunitgLab = Label(unitWin, text = 'Time sampling')
        unitTimeSampunitgLab.configure(bg= 'white')
        unitTimeSampunitgLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        unitTimeSampunitgEntry = Entry(unitWin)
        unitTimeSampunitgEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitTimeSampunitgEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))

        unitTimeStartLab = Label(unitWin, text = 'UnitStep Init Time')
        unitTimeStartLab.configure(bg= 'white')
        unitTimeStartLab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        unitTimeStartEntry = Entry(unitWin)
        unitTimeStartEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitTimeStartEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        unitAmplitudLab = Label(unitWin, text = 'Amplitud')
        unitAmplitudLab.configure(bg= 'white')
        unitAmplitudLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        unitAmplitudEntry = Entry(unitWin)
        unitAmplitudEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitAmplitudEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))


        unitValueTLab = Label(unitWin, text = 'Operations Values')
        unitValueTLab.configure(bg= 'gray')
        unitValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        unitScalationTLab = Label(unitWin, text = 'Scalation(t)')
        unitScalationTLab.configure(bg= 'white')
        unitScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        unitScalationTEntry = Entry(unitWin)
        unitScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        unitScalationALab = Label(unitWin, text = 'Scalation(A)')
        unitScalationALab.configure(bg= 'white')
        unitScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        unitScalationAEntry = Entry(unitWin)
        unitScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        unitDesplacementTLab = Label(unitWin, text = 'Desplacement(t)')
        unitDesplacementTLab.configure(bg= 'white')
        unitDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        unitDesplacementTEntry = Entry(unitWin)
        unitDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        unitDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def unitShowGraph():

            if unitScalationAEntry.get() == '':
                unitScalationAValue = 1
            else :
                unitScalationAValue = float(unitScalationAEntry.get())
            if unitScalationTEntry.get() ==  '':
                unitScalationTValue= 1
            else:
                unitScalationTValue= float(unitScalationTEntry.get())
            if unitDesplacementTEntry.get() == '':
                unitDesplacementTValue = 0
            else:
                unitDesplacementTValue = float(unitDesplacementTEntry.get())

            unitTimeInitValue = float(unitTimeInitEntry.get())
            unitTimeSampunitgValue = float(unitTimeSampunitgEntry.get())
            unitTimeFinalValue = float(unitTimeFinalEntry.get())
            unitTimeStartValue = float(unitTimeStartEntry.get())
            amplitudValue = float(unitAmplitudEntry.get())

            unitTime = np.arange(unitTimeInitValue, unitTimeFinalValue, 1/unitTimeSampunitgValue)
            unitGenerator = np.piecewise(unitTime,unitTime>=unitTimeStartValue,[1*amplitudValue,0])

            
            if unitScalationAEntry.get() or unitScalationTEntry.get() or  unitDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((unitTime),unitGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/unitScalationTValue*(unitTime-unitDesplacementTValue), unitScalationAValue*unitGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot((unitTime),unitGenerator )
                plt.plot(1/unitScalationTValue*(unitTime-unitDesplacementTValue), unitScalationAValue*unitGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('Overlapping signals')


                plt.show()
            else:
                
                
                plt.plot((unitTime),unitGenerator )
                plt.xlabel('t(s)')
                plt.show()

        unitShowGraphBtn = Button(unitWin, text="Show Graph", command = unitShowGraph)
        unitShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        unitShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        unitWin.mainloop()

    if choose.get()== 'Delta' :
        deltWin= Tk()
        deltWin.title(' Delta Singal')
        deltWin.geometry('600x400')
        deltWin.resizable(0,0)
        deltWin.config(bg= 'white', padx = 50, pady= 50)

        deltTimeInitLab = Label(deltWin, text = 'Time Init')
        deltTimeInitLab.configure(bg= 'white')
        deltTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        deltTimeInitEntry = Entry(deltWin)
        deltTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        deltTimeFinalLab = Label(deltWin, text = 'Time Final')
        deltTimeFinalLab.configure(bg= 'white')
        deltTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        deltTimeFinalEntry = Entry(deltWin)
        deltTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        deltTimeSampdeltgLab = Label(deltWin, text = 'Time sampling')
        deltTimeSampdeltgLab.configure(bg= 'white')
        deltTimeSampdeltgLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        deltTimeSampdeltgEntry = Entry(deltWin)
        deltTimeSampdeltgEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltTimeSampdeltgEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))

        deltTimeStartLab = Label(deltWin, text = 'Delta Init Time')
        deltTimeStartLab.configure(bg= 'white')
        deltTimeStartLab.grid(row = 4, column = 1, padx = (1,1), pady= (5,5))
        deltTimeStartEntry = Entry(deltWin)
        deltTimeStartEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltTimeStartEntry.grid(row= 4 ,column= 2, padx=(1,1), pady= (5,5))

        deltAmplitudLab = Label(deltWin, text = 'Amplitud')
        deltAmplitudLab.configure(bg= 'white')
        deltAmplitudLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        deltAmplitudEntry = Entry(deltWin)
        deltAmplitudEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltAmplitudEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))


        deltValueTLab = Label(deltWin, text = 'Operations Values')
        deltValueTLab.configure(bg= 'gray')
        deltValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        deltScalationTLab = Label(deltWin, text = 'Scalation(t)')
        deltScalationTLab.configure(bg= 'white')
        deltScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        deltScalationTEntry = Entry(deltWin)
        deltScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        deltScalationALab = Label(deltWin, text = 'Scalation(A)')
        deltScalationALab.configure(bg= 'white')
        deltScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        deltScalationAEntry = Entry(deltWin)
        deltScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        deltDesplacementTLab = Label(deltWin, text = 'Desplacement(t)')
        deltDesplacementTLab.configure(bg= 'white')
        deltDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        deltDesplacementTEntry = Entry(deltWin)
        deltDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        deltDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def deltShowGraph():

            if deltScalationAEntry.get() == '':
                deltScalationAValue = 1
            else :
                deltScalationAValue = float(deltScalationAEntry.get())
            if deltScalationTEntry.get() ==  '':
                deltScalationTValue= 1
            else:
                deltScalationTValue= float(deltScalationTEntry.get())
            if deltDesplacementTEntry.get() == '':
                deltDesplacementTValue = 0
            else:
                deltDesplacementTValue = float(deltDesplacementTEntry.get())

            deltTimeInitValue = float(deltTimeInitEntry.get())
            deltTimeSampdeltgValue = float(deltTimeSampdeltgEntry.get())
            deltTimeFinalValue = float(deltTimeFinalEntry.get())
            deltTimeStartValue = float(deltTimeStartEntry.get())
            amplitudValue = float(deltAmplitudEntry.get())

            deltTime = np.arange(deltTimeInitValue, deltTimeFinalValue, 1/deltTimeSampdeltgValue)
            deltPart1 = np.piecewise(deltTime,deltTime>=deltTimeStartValue,[1*amplitudValue,0])
            deltPart2 = np.piecewise(deltTime,deltTime>=deltTimeStartValue+0.001,[1*amplitudValue,0])
            deltGenerator = deltPart1 - deltPart2
            

            
            if deltScalationAEntry.get() or deltScalationTEntry.get() or  deltDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((deltTime),deltGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/deltScalationTValue*(deltTime-deltDesplacementTValue), deltScalationAValue*deltGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot((deltTime),deltGenerator )
                plt.plot(1/deltScalationTValue*(deltTime-deltDesplacementTValue), deltScalationAValue*deltGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('Overlapping signals')
                
                plt.show()
            else:
                
                
                plt.plot((deltTime),deltGenerator )
                plt.xlabel('t(s)')
                plt.show()

        deltShowGraphBtn = Button(deltWin, text="Show Graph", command = deltShowGraph)
        deltShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        deltShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        deltWin.mainloop()

    if choose.get()== 'Triangular' :
        triantWin= Tk()
        triantWin.title(' Triangular Singal')
        triantWin.geometry('600x400')
        triantWin.resizable(0,0)
        triantWin.config(bg= 'white', padx = 50, pady= 50)

        triantTimeInitLab = Label(triantWin, text = 'Time Init')
        triantTimeInitLab.configure(bg= 'white')
        triantTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        triantTimeInitEntry = Entry(triantWin)
        triantTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        triantTimeFinalLab = Label(triantWin, text = 'Time Final')
        triantTimeFinalLab.configure(bg= 'white')
        triantTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        triantTimeFinalEntry = Entry(triantWin)
        triantTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        triantTimeSamptriantgLab = Label(triantWin, text = 'Time sampling')
        triantTimeSamptriantgLab.configure(bg= 'white')
        triantTimeSamptriantgLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        triantTimeSamptriantgEntry = Entry(triantWin)
        triantTimeSamptriantgEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantTimeSamptriantgEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))


        triantAmplitudLab = Label(triantWin, text = 'Amplitud')
        triantAmplitudLab.configure(bg= 'white')
        triantAmplitudLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        triantAmplitudEntry = Entry(triantWin)
        triantAmplitudEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantAmplitudEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))


        triantValueTLab = Label(triantWin, text = 'Operations Values')
        triantValueTLab.configure(bg= 'gray')
        triantValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        triantScalationTLab = Label(triantWin, text = 'Scalation(t)')
        triantScalationTLab.configure(bg= 'white')
        triantScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        triantScalationTEntry = Entry(triantWin)
        triantScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        triantScalationALab = Label(triantWin, text = 'Scalation(A)')
        triantScalationALab.configure(bg= 'white')
        triantScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        triantScalationAEntry = Entry(triantWin)
        triantScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        triantDesplacementTLab = Label(triantWin, text = 'Desplacement(t)')
        triantDesplacementTLab.configure(bg= 'white')
        triantDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        triantDesplacementTEntry = Entry(triantWin)
        triantDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        triantDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def triantShowGraph():

            if triantScalationAEntry.get() == '':
                triantScalationAValue = 1
            else :
                triantScalationAValue = float(triantScalationAEntry.get())
            if triantScalationTEntry.get() ==  '':
                triantScalationTValue= 1
            else:
                triantScalationTValue= float(triantScalationTEntry.get())
            if triantDesplacementTEntry.get() == '':
                triantDesplacementTValue = 0
            else:
                triantDesplacementTValue = float(triantDesplacementTEntry.get())

            triantTimeInitValue = float(triantTimeInitEntry.get())
            triantTimeSamptriantgValue = float(triantTimeSamptriantgEntry.get())
            triantTimeFinalValue = float(triantTimeFinalEntry.get())
            amplitudValue = float(triantAmplitudEntry.get())

            triantTime = np.arange(triantTimeInitValue, triantTimeFinalValue, 1/triantTimeSamptriantgValue)
            triantGenerator = sp.sawtooth(triantTime)* amplitudValue
            

            
            if triantScalationAEntry.get() or triantScalationTEntry.get() or  triantDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((triantTime),triantGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/triantScalationTValue*(triantTime-triantDesplacementTValue), triantScalationAValue*triantGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot((triantTime),triantGenerator )
                plt.plot(1/triantScalationTValue*(triantTime-triantDesplacementTValue), triantScalationAValue*triantGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('Overlapping Signals')
                plt.show()
            else:
                
                
                plt.plot((triantTime),triantGenerator )
                plt.xlabel('t(s)')
                plt.show()

        triantShowGraphBtn = Button(triantWin, text="Show Graph", command = triantShowGraph)
        triantShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        triantShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        triantWin.mainloop()  

    if choose.get()== 'Square' :
        sqWin= Tk()
        sqWin.title('Square Singal')
        sqWin.geometry('600x400')
        sqWin.resizable(0,0)
        sqWin.config(bg= 'white', padx = 50, pady= 50)

        sqTimeInitLab = Label(sqWin, text = 'Time Init')
        sqTimeInitLab.configure(bg= 'white')
        sqTimeInitLab.grid(row = 1, column = 1, padx = (1,1), pady= (5,5))
        sqTimeInitEntry = Entry(sqWin)
        sqTimeInitEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqTimeInitEntry.grid(row= 1 ,column= 2, padx=(1,1), pady= (5,5))

        sqTimeFinalLab = Label(sqWin, text = 'Time Final')
        sqTimeFinalLab.configure(bg= 'white')
        sqTimeFinalLab.grid(row = 2, column = 1, padx = (1,1), pady= (5,5))
        sqTimeFinalEntry = Entry(sqWin)
        sqTimeFinalEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqTimeFinalEntry.grid(row= 2 ,column= 2, padx=(1,1), pady= (5,5))

        sqTimeSampsqgLab = Label(sqWin, text = 'Time sampling')
        sqTimeSampsqgLab.configure(bg= 'white')
        sqTimeSampsqgLab.grid(row = 3, column = 1, padx = (1,1), pady= (5,5))
        sqTimeSampsqgEntry = Entry(sqWin)
        sqTimeSampsqgEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqTimeSampsqgEntry.grid(row= 3 ,column= 2, padx=(1,1), pady= (5,5))


        sqAmplitudLab = Label(sqWin, text = 'Amplitud')
        sqAmplitudLab.configure(bg= 'white')
        sqAmplitudLab.grid(row = 5, column = 1, padx = (1,1), pady= (5,5))
        sqAmplitudEntry = Entry(sqWin)
        sqAmplitudEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqAmplitudEntry.grid(row= 5 ,column= 2, padx=(1,1), pady= (5,5))


        sqValueTLab = Label(sqWin, text = 'Operations Values')
        sqValueTLab.configure(bg= 'gray')
        sqValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        sqScalationTLab = Label(sqWin, text = 'Scalation(t)')
        sqScalationTLab.configure(bg= 'white')
        sqScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        sqScalationTEntry = Entry(sqWin)
        sqScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        sqScalationALab = Label(sqWin, text = 'Scalation(A)')
        sqScalationALab.configure(bg= 'white')
        sqScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        sqScalationAEntry = Entry(sqWin)
        sqScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        sqDesplacementTLab = Label(sqWin, text = 'Desplacement(t)')
        sqDesplacementTLab.configure(bg= 'white')
        sqDesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        sqDesplacementTEntry = Entry(sqWin)
        sqDesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sqDesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def sqShowGraph():

            if sqScalationAEntry.get() == '':
                sqScalationAValue = 1
            else :
                sqScalationAValue = float(sqScalationAEntry.get())
            if sqScalationTEntry.get() ==  '':
                sqScalationTValue= 1
            else:
                sqScalationTValue= float(sqScalationTEntry.get())
            if sqDesplacementTEntry.get() == '':
                sqDesplacementTValue = 0
            else:
                sqDesplacementTValue = float(sqDesplacementTEntry.get())

            sqTimeInitValue = float(sqTimeInitEntry.get())
            sqTimeSampsqgValue = float(sqTimeSampsqgEntry.get())
            sqTimeFinalValue = float(sqTimeFinalEntry.get())
            amplitudValue = float(sqAmplitudEntry.get())

            sqTime = np.arange(sqTimeInitValue, sqTimeFinalValue, 1/sqTimeSampsqgValue)
            sqGenerator = sp.square(sqTime)*amplitudValue
            

            
            if sqScalationAEntry.get() or sqScalationTEntry.get() or  sqDesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((sqTime),sqGenerator )
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/sqScalationTValue*(sqTime-sqDesplacementTValue), sqScalationAValue*sqGenerator , color = "orange")
                plt.title('Transformated Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,4)
                plt.plot((sqTime),sqGenerator )
                plt.plot(1/sqScalationTValue*(sqTime-sqDesplacementTValue), sqScalationAValue*sqGenerator , color = "orange")
                plt.xlabel('t(s)')
                plt.title('Overlapping signals')
                plt.show()
            else:
                
                
                plt.plot((sqTime),sqGenerator )
                plt.xlabel('t(s)')
                plt.show()

        sqShowGraphBtn = Button(sqWin, text="Show Graph", command = sqShowGraph)
        sqShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        sqShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        sqWin.mainloop() 

    if choose.get()== 'sust1' :
        sust1Win= Tk()
        
        sust1ValueTLab = Label(sust1Win, text = 'Operations Values')
        sust1ValueTLab.configure(bg= 'gray')
        sust1ValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        sust1ScalationTLab = Label(sust1Win, text = 'Scalation(t)')
        sust1ScalationTLab.configure(bg= 'white')
        sust1ScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        sust1ScalationTEntry = Entry(sust1Win)
        sust1ScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sust1ScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        sust1ScalationALab = Label(sust1Win, text = 'Scalation(A)')
        sust1ScalationALab.configure(bg= 'white')
        sust1ScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        sust1ScalationAEntry = Entry(sust1Win)
        sust1ScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sust1ScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        sust1DesplacementTLab = Label(sust1Win, text = 'Desplacement(t)')
        sust1DesplacementTLab.configure(bg= 'white')
        sust1DesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        sust1DesplacementTEntry = Entry(sust1Win)
        sust1DesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sust1DesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def sust1ShowGraph():

            if sust1ScalationAEntry.get() == '':
                sust1ScalationAValue = 1
            else :
                sust1ScalationAValue = float(sust1ScalationAEntry.get())
            if sust1ScalationTEntry.get() ==  '':
                sust1ScalationTValue= 1
            else:
                sust1ScalationTValue= float(sust1ScalationTEntry.get())
            if sust1DesplacementTEntry.get() == '':
                sust1DesplacementTValue = 0
            else:
                sust1DesplacementTValue = float(sust1DesplacementTEntry.get())

            

           
            
            sust1TimeExpo2 = np.arange(6,9,1/100)
            sust1ExpoGenertor2 = (np.exp(sust1TimeExpo2*0.3))*1-6
            tlin = np.arange (3,6,1/100 )
            tlin2 = np.arange (9,12,1/100 )
            lingen = -3*tlin+ 18
            lingen2 = -3*tlin2-3+ 18 +20.8
            tq = np.arange (0,3, 1/100)
            quadraticGenerator= (-1*((tq-3)**2)+ 9) 


            


            
            

            
            if sust1ScalationAEntry.get() or sust1ScalationTEntry.get() or  sust1DesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((sust1TimeExpo2),sust1ExpoGenertor2 )
                plt.plot((tlin),lingen )
                plt.plot((tlin2),lingen2 )
                plt.plot((tq),quadraticGenerator)
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/sust1ScalationTValue*(sust1TimeExpo2-sust1DesplacementTValue),sust1ScalationAValue*sust1ExpoGenertor2 )
                plt.plot(1/sust1ScalationTValue*(tlin-sust1DesplacementTValue),sust1ScalationAValue*lingen )
                plt.plot(1/sust1ScalationTValue*(tlin2-sust1DesplacementTValue),sust1ScalationAValue*lingen2 )
                plt.plot(1/sust1ScalationTValue*(tq-sust1DesplacementTValue),sust1ScalationAValue*quadraticGenerator)
                plt.show()
               
                
            else:
                
                
                
                plt.plot((sust1TimeExpo2),sust1ExpoGenertor2 )
                plt.plot((tlin),lingen )
                plt.plot((tlin2),lingen2 )
                plt.plot((tq),quadraticGenerator)
                plt.xlim(0, 12)
                plt.ylim(0,12 )
               
                
                
                plt.xlabel('t(s)')
                plt.show()

        sust1ShowGraphBtn = Button(sust1Win, text="Show Graph", command = sust1ShowGraph)
        sust1ShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        sust1ShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        sust1Win.mainloop() 

    if choose.get()== 'sust2' :
        sust2Win= Tk()
        
        sust2ValueTLab = Label(sust2Win, text = 'Operations Values')
        sust2ValueTLab.configure(bg= 'gray')
        sust2ValueTLab.grid(row = 1, column = 3, padx = (1,1), pady= (5,5))


        sust2ScalationTLab = Label(sust2Win, text = 'Scalation(t)')
        sust2ScalationTLab.configure(bg= 'white')
        sust2ScalationTLab.grid(row = 2, column = 3, padx = (1,1), pady= (5,5))
        sust2ScalationTEntry = Entry(sust2Win)
        sust2ScalationTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sust2ScalationTEntry.grid(row= 2 ,column= 4, padx=(1,1), pady= (5,5))

        sust2ScalationALab = Label(sust2Win, text = 'Scalation(A)')
        sust2ScalationALab.configure(bg= 'white')
        sust2ScalationALab.grid(row = 3, column = 3, padx = (1,1), pady= (5,5))
        sust2ScalationAEntry = Entry(sust2Win)
        sust2ScalationAEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sust2ScalationAEntry.grid(row= 3 ,column= 4, padx=(1,1), pady= (5,5))

        sust2DesplacementTLab = Label(sust2Win, text = 'Desplacement(t)')
        sust2DesplacementTLab.configure(bg= 'white')
        sust2DesplacementTLab.grid(row = 4, column = 3, padx = (1,1), pady= (5,5))
        sust2DesplacementTEntry = Entry(sust2Win)
        sust2DesplacementTEntry.configure(bg= 'white', bd= 2, relief = 'sunken')
        sust2DesplacementTEntry.grid(row= 4,column= 4, padx=(1,1), pady= (5,5))

        def sust2ShowGraph():

            if sust2ScalationAEntry.get() == '':
                sust2ScalationAValue = 1
            else :
                sust2ScalationAValue = float(sust2ScalationAEntry.get())
            if sust2ScalationTEntry.get() ==  '':
                sust2ScalationTValue= 1
            else:
                sust2ScalationTValue= float(sust2ScalationTEntry.get())
            if sust2DesplacementTEntry.get() == '':
                sust2DesplacementTValue = 0
            else:
                sust2DesplacementTValue = float(sust2DesplacementTEntry.get())

            

           
            
            t1 = np.arange(6,9,1/100)
            st= (((t1-9)**2))-0
            t2 = np.arange (3,6,1/100 )
            t3 = np.arange (9,12,1/100 )
            st2 = 3*t2+ -9
            st3 = 3*t3-27
            t4 = np.arange (0,3, 1/100)
            quadraticGenerator= (-1*((t4)**2)) +9


            


            
            

            
            if sust2ScalationAEntry.get() or sust2ScalationTEntry.get() or  sust2DesplacementTEntry.get() != '':
                plt.figure(figsize = (9,9))
                plt.subplot(2,2,1)
                plt.plot((t1),st )
                plt.plot((t2),st2 )
                plt.plot((t3),st3 )
                plt.plot((t4),quadraticGenerator)
                plt.title('Original Signal')
                plt.xlabel('t(s)')
                plt.subplot(2,2,3)
                plt.plot(1/sust2ScalationTValue*(t1-sust2DesplacementTValue),sust2ScalationAValue*st )
                plt.plot(1/sust2ScalationTValue*(t2-sust2DesplacementTValue),sust2ScalationAValue*st2 )
                plt.plot(1/sust2ScalationTValue*(t3-sust2DesplacementTValue),sust2ScalationAValue*st3 )
                plt.plot(1/sust2ScalationTValue*(t4-sust2DesplacementTValue),sust2ScalationAValue*quadraticGenerator)
                plt.show()
               
                
            else:
                
                
                
                plt.plot((t1),st )
                plt.plot((t2),st2 )
                plt.plot((t3),st3 )
                plt.plot((t4),quadraticGenerator)
                
               
                
                
                plt.xlabel('t(s)')
                plt.show()

        sust2ShowGraphBtn = Button(sust2Win, text="Show Graph", command = sust2ShowGraph)
        sust2ShowGraphBtn.grid(row=8, column=1, padx=(1, 1), pady=(10, 10))
        sust2ShowGraphBtn.config(cursor='hand2', bd='5', relief='groove')

        sust2Win.mainloop() 

chooseSignalBtn= Button(main, text = 'Acept', command= showGraphicWindows )
chooseSignalBtn.configure(cursor = 'hand2',bg= 'white', bd = 3)
chooseSignalBtn.grid(sticky = 'w',row = 3, column = 1, padx = (2,2), pady= (10,10))
chooseSignalBtn= Button(main, text = 'Acept', command= showGraphicWindows )
chooseSignalBtn.configure(cursor = 'hand2',bg= 'white', bd = 3)
chooseSignalBtn.grid(sticky = 'w',row = 3, column = 1, padx = (2,2), pady= (10,10))






main.mainloop()




