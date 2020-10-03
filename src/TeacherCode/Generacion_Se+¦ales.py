import numpy as np
from matplotlib import pyplot as plt

# u0 = np.piecewise(t,t>=-0.3,[2,1])  #SEÑAL ESCALÓN
# plt.figure(1)
# plt.plot(t,u0)
# plt.xlabel('t')
# plt.ylabel('escalon u(t)')
# plt.show()


# imp = 0
# delta = np.piecewise(t,t>=0,[1,0])
# delta_dt = np.piecewise(t,t>=imp+dt,[1,0])
# unimpulso = delta - delta_dt      #SEÑAL IMPULSO
# plt.figure(2)
# plt.plot(t,unimpulso)
# plt.show()





# from scipy import signal as sp
# t1 = np.arange(0,10, 0.001)
# w = sp.square(t1)    #SEÑAL CUADRADA
# plt.plot(t1,w)
# plt.show()

# x = sp.sawtooth(t1) #SEÑAL TRIANGULAR
# plt.plot(t1,x) ## Sirve para graficar una función sobre otra
# plt.show()
# h = np.arange((min(t1)+ min(t1)), (max(t1) + max(t1)))
# plt.plot(h, np.convolve(w,x))
# plt.title('lafsdafsd')
# plt.show()


dt = 0.001
t = np.arange(0,1,dt) # VECTOR DE TIEMPO

t2 = np.arange(0,2,0.001)
y = np.sin(2*np.pi*t)*6  # SEÑAL TRIGONOMÉTRICA
plt.plot(t,y)
plt.title('Gráfica')
plt.show()

z = np.exp(t2)  #SEÑAL EXPONENCIAL
plt.plot(t2,z)
plt.show()

tc = max(t)+ max(t2)
tl = min(t) + min(t2)
dss = 0.001
t3 = np.arange(tl,tc+dss,dss)
conv = np.convolve(z,y)
plt.plot(t3, conv)
plt.show()