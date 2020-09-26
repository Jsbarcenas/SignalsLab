import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

# Aquí creo la interfaz de usuario.
gui = Tk()
gui.title('EJEMPLO - GUIDE EN PYTHON')
gui.configure(background='white', padx=5, pady=5)
gui.geometry("500x300")


# Tiempo Inicial
lab_ini = Label(gui, text="Tiempo Inicial:")
lab_ini.configure(background = 'white')
lab_ini.grid(row=1, column=1, padx=(1, 1), pady=(5, 5))
t_ini = Entry(gui)
t_ini.configure(background = 'white')
t_ini.grid(row=1, column=2, padx=(1, 1), pady=(5, 5))
t_ini.config(width=10)

# Tiempo Final
lab_fin = Label(gui, text="Tiempo Final:")
lab_fin.configure(background = 'white')
lab_fin.grid(row=2, column=1, padx=(1, 1), pady=(5, 5))
t_fin = Entry(gui)
t_fin.configure(background = 'white')
t_fin.grid(row=2, column=2, padx=(1, 1), pady=(5, 5))
t_fin.config(width=10)

# Tasa de muestreo
lab_ts = Label(gui, text="Tasa de Muestreo:")
lab_ts.configure(background = 'white')
lab_ts.grid(row=3, column=1, padx=(1, 1), pady=(5, 5))
ts = Entry(gui)
ts.configure(background = 'white')
ts.grid(row=3, column=2, padx=(1, 1), pady=(5, 5))
ts.config(width=10)

# Etiqueta
lab_1 = Label(gui, text="Seleccione el tipo de señal")
lab_1.configure(background = 'white')
lab_1.grid(row=4, column=1, padx=(1, 1), pady=(10, 10))

fun = StringVar(gui)
fun.set('Seleccione señal...')
menu = OptionMenu(gui, fun, 'Seleccione señal...','Trigonometrica', 'Exponencial','Logaritmica')
menu.grid(row=4, column=2, padx=(1, 1), pady=(10, 10))

def Mostrar_Grafica():
    ti = float(t_ini.get())
    tf = float(t_fin.get())
    Ts = float(ts.get())
    t = np.arange(ti,tf,Ts)
    if fun.get() == 'Exponencial':
        y = np.exp(t)
    if fun.get() == 'Logaritmica':
        y = np.log(t)
    if fun.get() == 'Trigonometrica':
        y = np.sin(2*np.pi*t)
    plt.figure(1)
    plt.clf()
    plt.title('Señal')
    plt.plot(t, y)
    plt.gcf().canvas.draw()

    plt.figure(2)
    plt.clf()
    plt.title('hola')
    plt.plot(t, y)
    plt.gcf().canvas.draw()
    
# Button
btn = Button(gui, text="Mostrar Gráfica", command=Mostrar_Grafica)
btn.grid(row=5, column=1, padx=(1, 1), pady=(10, 10))

# Aquí defino mi canvas para graficar la señal.
fig = plt.figure(figsize=(3,2))
canv = FigureCanvasTkAgg(fig, master=gui)
canv.get_tk_widget().grid(row=5, column=2, padx=(1, 1), pady=(10, 10))

fig1 = plt.figure(figsize=(3,2))
canv = FigureCanvasTkAgg(fig1, master=gui)
canv.get_tk_widget().grid(row=6, column=2, padx=(1, 1), pady=(10, 10))

gui.mainloop()