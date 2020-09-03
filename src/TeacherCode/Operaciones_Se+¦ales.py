import numpy as np
from matplotlib import pyplot as plt

t_ini = -1
t_fin = 1
dt = 0.001
t = np.arange(t_ini,t_fin,dt) # VECTOR DE TIEMPO


#ESCALAMIENTO DE AMPLITUD
A = 2
Y_Amp = A*np.sin(2*np.pi*t)
plt.subplot(211)
plt.plot(t,Y_Amp)
plt.title('Señal Original')
plt.subplot(212)
plt.plot(t,2*Y_Amp)
plt.show()


#ESCALAMIENTO DE TIEMPO
a = 2
Y_Time = np.sin(2*np.pi*a*t)
plt.subplot(211)
plt.plot(t,Y_Time)
plt.title('Señal Original')
plt.subplot(212)
plt.plot(t,Y_Time)
plt.show()

#DESPLAZAMIENTO DE TIEMPO
t0 = 4
Y_Des = np.sin(2*np.pi*t-t0)
plt.plot(t,Y_Des)
plt.show()

