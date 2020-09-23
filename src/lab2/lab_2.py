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
main.config(bg= 'white')
main.geometry('600x400')
main.resizable(0,0)
main.title('Signal Convolutions')
titleLabel= Label(main, text = 'Laboratory 2th-- Signal Convolutions')
titleLabel.config( padx = 5, pady= 5)
titleLabel.place(x = 200)

##Marcos de opcion 1
function1 = LabelFrame(main, text= 'x(t)/x[n]')
function1.config(width = 140, height = 50)
function1.place(y= 50)
labelTitleF1= Label(function1, text = 'stand by function',pady= 10)
labelTitleF1.config(width= 40)
labelTitleF1.grid(row = 0, column= 0)


def callbackF1 (event):
    if selectF1Lab.get() == "option1":
        entryStateE = "enable"
entryState = "disable"
entryStateE= "disable"
selectF1Lab = ttk.Combobox(function1, values = ["option1", "option2", "option"],state="readonly")
selectF1Lab.grid(sticky = 'w', row= 1, column = 0)
selectF1Lab.bind("<<ComboboxSelected>>", callbackF1)

amplitudF1lab = Label(function1, text = 'Amplitud')
amplitudF1lab.config(pady = 5, padx = 1)
amplitudF1lab.grid(sticky = 'w', row = 2, column= 0)
amplitudF1Entry = Entry(function1, state = entryState)
amplitudF1Entry.config(bd = 2, width= 5)
amplitudF1Entry.place( x = 60, y = 65)

periodF1Lab= Label(function1, text ="Period")
periodF1Lab.config(pady = 5, padx = 1)
periodF1Lab.grid(sticky = 'w', row = 3, column= 0)
periodF1Entry = Entry(function1, state = entryState)
periodF1Entry.config(bg = 'white',bd = 2, width= 5)
periodF1Entry.place( x = 60, y = 95)

exponentF1Lab= Label(function1, text ="Exponent")
exponentF1Lab.config(pady = 5, padx = 1)
exponentF1Lab.place(x= 100, y = 60)
exponentF1Entry = Entry(function1, state = entryStateE)
exponentF1Entry.config(bg = 'white',bd = 2, width= 5)
exponentF1Entry.place( x = 160, y = 65)






##Marco de opcion 2
function2 = LabelFrame(main, text= 'x(t)/x[n]')
function2.config(width = 140, height = 50)
function2.place(y= 50, x = 310)
labelTitleF2= Label(function2, text = 'Moving Function',pady= 10)
labelTitleF2.config(width= 40)
labelTitleF2.grid(row = 0, column= 0)




main.mainloop()



