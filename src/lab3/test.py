from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from tkinter import *
from scipy import signal as sp

main = Tk()
main.title('Taller Series')
main.configure(background='#013B7D', padx=30, pady=10)
main.geometry('1150x700+0+20')
 
frame_parametros= Frame(main)
frame_parametros.grid(row=0, column=0,columnspan=2, padx=5, pady=5,rowspan=3,sticky='w')
frame_parametros.config(width='360',heigh='200',background='#1E60AB')
frame_parametros.grid_propagate(False)
Func_do = StringVar(frame_parametros)
Func_do.set('Señal')

dom = OptionMenu(frame_parametros, Func_do, 
	'Señal 1',
	'Señal 2',
	'Señal 3',
	'Señal 4',
	'Señal 5'
	)
dom.grid(row=0, column=0, padx=(10, 10), pady=(10, 10),columnspan=2)
dom.config(width=20,background='#47BFF0')

caja_1 = Entry(frame_parametros)
caja_1.configure(background = 'white')
caja_1.config(width=10)
caja_1.grid(row=0,column=3)

E_caja_1 =Label(frame_parametros, text="Ti")
E_caja_1 .configure(background = 'white')
E_caja_1 .config(width=10)
E_caja_1.grid(row=0,column=2)






caja_2 = Entry(frame_parametros)
caja_2.configure(background = 'white')
caja_2.config(width=10)
caja_2.grid(row=1,column=3,padx=5,pady=5)

E_caja_2 = Label(frame_parametros, text="Tf")
E_caja_2.configure(background = 'white')
E_caja_2.config(width=10)
E_caja_2.grid(row=1,column=2,padx=5,pady=5)





caja_3 = Entry(frame_parametros)
caja_3.configure(background = 'white')
caja_3.config(width=10)
caja_3.grid(row=2,column=3 ,padx=5,pady=5)

E_caja_3 = Label(frame_parametros, text="A")
E_caja_3.configure(background = 'white')
E_caja_3.config(width=10)
E_caja_3.grid(row=2,column=2,padx=5,pady=5)




caja_4= Entry(frame_parametros)
caja_4.configure(background = 'white')
caja_4.config(width=10)
caja_4.grid(row=3,column=3,padx=5,pady=5)

E_caja_4 = Label(frame_parametros, text="T")
E_caja_4.configure(background = 'white')
E_caja_4.config(width=10)
E_caja_4.grid(row=3,column=2,padx=5,pady=5)


caja_5= Entry(frame_parametros)
caja_5.configure(background = 'white')
caja_5.config(width=10)
caja_5.grid(row=4,column=3,padx=5,pady=5)

E_caja_5 = Label(frame_parametros, text="N")
E_caja_5.configure(background = 'white')
E_caja_5.config(width=10)
E_caja_5.grid(row=4,column=2,padx=5,pady=5)

def graficar() :
	global tx, x
	ti=float(caja_1.get())
	tf=float(caja_2.get())
	a=float(caja_3.get())
	f=Func_do.get()
	dt=0.01

	if f=="Señal 1":
		t1=np.arange(0,3,dt)
		t2=np.arange(3,6,dt)
		t3=np.arange(6,9,dt)
		x1=np.zeros(len(t1))
		x2=np.exp(t2-3)-1
		x3=np.zeros(len(t3))+x2[len(x2)-1]

		tx= np.concatenate((t1,t2,t3),axis=None)
		x= a*np.concatenate((x1,x2,x3),axis=None)
		tt=tx/9*(tf-ti)+ti

	if f=="Señal 2":
		t1=np.arange(0,10/3,dt)
		t2=np.arange(10/3,2*10/3,dt)
		t3=np.arange(2*10/3,10,dt)
		x1=np.zeros(len(t1))+10/3
		x2=-(t2-10/3*2)
		x3=np.zeros(len(t3))

		tx= np.concatenate((t1,t2,t3),axis=None)
		x= a*np.concatenate((x1,x2,x3),axis=None)
		tt=tx/10*(tf-ti)+ti
	if f=="Señal 3":
		t1=np.arange(0,10/3,dt)
		t2=np.arange(10/3,2*10/3,dt)
		t3=np.arange(2*10/3,10,dt)
		x1=t1
		x2=np.zeros(len(t2))+10/3
		x3=-(t3-10)

		tx= np.concatenate((t1,t2,t3),axis=None)
		x= a*np.concatenate((x1,x2,x3),axis=None)
		tt=tx/10*(tf-ti)+ti

	if f=="Señal 4":
		t1=np.arange(0,10/3,dt)
		t2=np.arange(10/3,2*10/3,dt)
		t3=np.arange(2*10/3,10,dt)
		x1=(np.exp(-t1)-1)*(-1)
		x2=(np.exp(-t1)-1)+max(x1)
		x3=(np.exp(-t1)-1)*(-1)

		tx= np.concatenate((t1,t2,t3),axis=None)
		x= a*np.concatenate((x1,x2,x3),axis=None)
		tt=tx/10*(tf-ti)+ti

	if f=="Señal 5":
		t1=np.arange(0,10/3,dt)
		t2=np.arange(10/3,2*10/3,dt)
		t3=np.arange(2*10/3,10,dt)
		x1=(np.exp(t1)-1)*(-1)
		x2=(np.exp(t1)-1)+min(x1)
		x3=(np.exp(t1)-1)*(-1)

		tx= np.concatenate((t1,t2,t3),axis=None)
		x= a*np.concatenate((x1,x2,x3),axis=None)
		tt=tx/10*(tf-ti)+ti



	plt.figure(1)
	plt.clf()
	plt.title('X(t)')
	plt.plot( tt,x)
	plt.grid()
	plt.gcf().canvas.draw()

def forr() :
	global tx,x
	dt = 0.01 #Vector de tiempo
	x = x#Señal cuadrática
	TT=float(caja_4.get())
	


	#Definimos parámetros para calcular las coeficientes de Fourier
	T = tx[len(tx)-1]+dt #Periodo
	Wo = 2*np.pi/T #Frecuencia
	n = int(caja_5.get()) #Número de armónicos
	Ak = np.zeros((n,1)) #Inicializamos el vector de coeficientes Ak
	Bk = np.zeros((n,1)) #Inicializamos el vector de coeficientes Bk
	m = len(tx) #Calculamos la dimensión de la señal

	Nk = np.arange(1,n+1)
	Ck = np.zeros((n,1)) #Inicializamos el vector del espectro de amplitud
	Phi_k = np.zeros((n,1)) #Inicializamos el vector del espectro de fase

	#Cálculo del coeficiente A0 (Valor medio)
	A0 = 0
	for i in range(1,m):
		A0 = A0 + (1/T)*x[i]*dt

	#Cálculo de los coeficientes Ak, Bk y el espectro de amplitud y fase
	for  i in range(1,n):
		for j in range(1,m):
			Ak[i] = Ak[i] + ((2/T)*x[j]*np.cos(i*tx[j]*Wo))*dt
			Bk[i] = Bk[i] + ((2/T)*x[j]*np.sin(i*tx[j]*Wo))*dt
		
		Ck[i] = ((Ak[i])**2 + (Bk[i])**2)**0.5 
		Phi_k[i] = abs(-1*np.arctan(Bk[i]/Ak[i]))

	#Reconstruimos la señal original usando los coeficientes de Fourier
	t1 = np.arange(0,2*T,0.01)
	xf = 0
	for i in range(1,n):
		xf = xf + Ak[i]*np.cos(i*Wo*t1) + Bk[i]*np.sin(i*Wo*t1)

	xf=xf+A0
	t1=t1-T
	t1=t1/T*TT

	plt.figure(2)
	plt.clf()
	plt.title('Señal Reconstruida')
	plt.plot(t1, xf)
	plt.grid()
	plt.gcf().canvas.draw()

	plt.figure(3)
	plt.clf()
	plt.title('Espectro en Fase')
	plt.stem(Nk, Phi_k)
	plt.grid()
	plt.gcf().canvas.draw()

	plt.figure(4)
	plt.clf()
	plt.title('Espectro en Magnitud')
	plt.stem(Nk, Ck)
	plt.grid()
	plt.gcf().canvas.draw()


botonframe_X = Button(frame_parametros, text="Graficar", command=graficar)
botonframe_X.grid(row=1, column=0, padx=10,pady=5)
botonframe_X.configure(width=20,background='#47BFF0')

boton= Button(frame_parametros, text="Serie de Fourier",command=forr)
boton.grid(row=2, column=0, padx=10,pady=5)
boton.configure(width=20,background='#47BFF0')


fig_1= plt.figure(figsize=(3.5,2),facecolor='#1E60AB')
canv_1 = FigureCanvasTkAgg(fig_1, master=main)
canv_1.get_tk_widget().grid(row=3,column=0, padx=10,pady=10,sticky='n')

fig_2= plt.figure(figsize=(3.5,2),facecolor='#1E60AB')
canv_2 = FigureCanvasTkAgg(fig_2, master=main)
canv_2.get_tk_widget().grid(row=4,column=0, padx=10,pady=10,sticky='n')

fig_3= plt.figure(figsize=(7.2,2),facecolor='#1E60AB')
canv_3 = FigureCanvasTkAgg(fig_3, master=main)
canv_3.get_tk_widget().grid(row=3,column=1, padx=10,pady=10,sticky='n',columnspan=2)

fig_4= plt.figure(figsize=(7.2,2),facecolor='#1E60AB')
canv_4 = FigureCanvasTkAgg(fig_4, master=main)
canv_4.get_tk_widget().grid(row=4,column=1, padx=10,pady=10,sticky='n',columnspan=2)


main.mainloop()