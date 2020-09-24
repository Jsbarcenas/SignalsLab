import numpy as np
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt

# aquí creo la interfaz de
gui = Tk()
gui.title('EJEMPLO - GUIDE EN PYTHON')
gui.configure(background='white', padx=50, pady=50)
gui.geometry("700x500")
hola = Label(gui, text = 'Hola')
hola.configure(bg = 'white')
hola.grid(row = 5, column = 8)
 
# Tiempo Inicial
lab_ini = Label(gui, text="Tiempo Inicial:")
lab_ini.configure(background='white')
lab_ini.grid(row=1, column=1, padx=(1, 1), pady=(5, 5))
t_ini = Entry(gui)
t_ini.configure(background='white', bd=2, relief='sunken')
t_ini.grid(row=7, column=2, padx=(1, 1), pady=(5, 5))
t_ini.config(width=10)

# Tiempo Final
lab_fin = Label(gui, text="Tiempo Final:")
lab_fin.configure(background='white')
lab_fin.grid(row=2, column=1, padx=(1, 1), pady=(5, 5))
t_fin = Entry(gui)
t_fin.configure(background='white')
t_fin.grid(row=2, column=2, padx=(1, 1), pady=(5, 5))
t_fin.config(width=10)

# Tasa de muestreo
lab_ts = Label(gui, text="Tasa de Muestreo:")
lab_ts.configure(background='white')
lab_ts.grid(row=3, column=1, padx=(1, 1), pady=(5, 5))
ts = Entry(gui)
ts.configure(background='white')
ts.grid(row=3, column=2, padx=(1, 1), pady=(5, 5))
ts.config(width=10)

# Etiqueta
lab_1 = Label(gui, text="Seleccione el tipo de señal")
lab_1.configure(background='white')
lab_1.grid(row=4, column=1, padx=(1, 1), pady=(10, 10))

fun = StringVar()
fun.set('Seleccione señal...')

menu = OptionMenu(gui, fun, 'Seleccione señal...',
                  'Trigonometrica', 'Exponencial', 'Logaritmica')
menu.grid(row=4, column=2, padx=(1, 1), pady=(10, 10))
menu.config(cursor='hand2')


def Mostrar_Grafica():
    ti = float(t_ini.get())
    tf = float(t_fin.get())
    Ts = float(ts.get())
    t = np.arange(ti, tf, Ts)
    if fun.get() == 'Exponencial':
        hola = Label(gui, text='aqupi estoy')
        hola.config(bg='white')
        hola.grid(row=6, column=5)
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


# Button
btn = Button(gui, text="Mostrar Gráfica", command=Mostrar_Grafica)
btn.grid(row=5, column=1, padx=(1, 1), pady=(10, 10))
btn.config(cursor='hand2', bd='5', relief='groove')

# Aquí defino mi canvas para graficar la señal.
fig = plt.figure(figsize=(3, 2))
canv = FigureCanvasTkAgg(fig, master=gui)
canv.get_tk_widget().grid(row=5, column=2, padx=(1, 1), pady=(10, 10))

gui.mainloop()


import tkinter as tk
from tkinter import ttk




import tkinter as tk
from tkinter import ttk

import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd


# DataFrame para ejemplo
df = pd.DataFrame({"Foo": (1, 5, 8, 7, 5, 1, 5),
                   "Bar": (4.25, 5, 6, 1.3, 1, 2.6, 3.7)}
                  )

# Creamos una figura y añadimos algunas gráficas en subplots
fig1 = Figure(figsize=(5, 5), dpi=100)
ax1 = fig1.add_subplot(311)
ax2 = fig1.add_subplot(312)
ax3 = fig1.add_subplot(313)
df.plot(ax=ax1)
df.plot.bar(ax=ax2)
df.plot.area(ax=ax3)


# Ventana principal
root = tk.Tk()

# Canvas  y barras de desplazamiento
canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
hsb = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)                 
vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(xscrollcommand=hsb.set)
canvas.configure(yscrollcommand=vsb.set)
hsb.pack(side="bottom", fill="x")
vsb.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Vamos a usar un ttk.Labelframe para contener FigureCanvasTkAgg
plot_frame = ttk.Labelframe(canvas, text='Plots')
canvas.create_window((4,4), window=plot_frame, anchor="nw", tags="plot_frame")
plot_frame.bind("<Configure>",
                lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
                )

# Creamos una instancia de FigureCanvas que renderizará la figura
canvas1 = FigureCanvasTkAgg(fig1, master=plot_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0, column=0)

root.mainloop()

