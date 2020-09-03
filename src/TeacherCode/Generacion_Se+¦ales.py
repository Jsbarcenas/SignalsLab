import numpy as np
from matplotlib import pyplot as plt

t_ini = -1
t_fin = 1
dt = 0.001
t = np.arange(t_ini,t_fin,dt) # VECTOR DE TIEMPO

y = np.sin(2*np.pi*t)  # SEÑAL TRIGONOMÉTRICA
plt.plot(t,y)
plt.title('Gráfica')
plt.show()

u0 = np.piecewise(t,t>=-0.3,[2,1])  #SEÑAL ESCALÓN
plt.figure(1)
plt.plot(t,u0)
plt.xlabel('t')
plt.ylabel('escalon u(t)')
plt.show()


imp = 0
delta = np.piecewise(t,t>=0,[1,0])
delta_dt = np.piecewise(t,t>=imp+dt,[1,0])
unimpulso = delta - delta_dt      #SEÑAL IMPULSO
plt.figure(2)
plt.plot(t,unimpulso)
plt.show()


z = np.exp(t)  #SEÑAL EXPONENCIAL
plt.plot(t,z)
plt.show()


from scipy import signal as sp
t1 = np.arange(-10,10,0.01)
w = sp.square(t1)    #SEÑAL CUADRADA
plt.plot(t1,w)
plt.show()

x = sp.sawtooth(t1)  #SEÑAL TRIANGULAR
plt.plot(t1,x, 'k',t1, unimpulso) ## Sirve para graficar una función sobre otra
plt.show()