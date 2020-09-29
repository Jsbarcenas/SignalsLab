# Graficas de funciones singulares
# from matplotlib.pyplot import *
# from numpy import *

# # funcion escalon unitario
# def u(t): return piecewise(t,[t<0.0,t>=0.0],[0,1])

# # funcion f(t)
# def f(t): return t*(u(t)-u(t-1))+2*u(t-1)
 
# t=linspace(-1,5,1000)
# plot(t,f(t),'k',label=r'$f(t)$',lw=2)
# xlim(-1,3);ylim(0,2.2)
# legend(loc='best')
# title(r'Funci\'on $f(t)=tu(t)-(t-1)u(t-1)+u(t-1)$')
# show()

# import numpy as np
# from matplotlib import pyplot as plt
# def ut(t):
#  return t*np.arange(0,5)


# t = np.arange(0,10,0.001)
# f= np.piecewise(t, t>0, [ut(5),0])
# plt.plot(t,f)
# plt.show()

# Señales modelo varias
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sp

tf = 10
ti = 3
td = tf -ti
tk = (td-ti)/2
tl = tk+ti
print(tk)
t=np.arange(ti,tf, 0.001)
y = np.piecewise(t,t>0,[1])
def u(t): return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
def f(t): return  (t-tk)*(u(t-tk)-u(t-tl))+ti*u(t-tl) 
plt.plot(t, f(t))
plt.show()


# tf = 30
# ti = 0
# td = tf -ti
# tk = (td-3)/2
# tl = tk+3
# tk2 = tl+5.5
# tl2= tk2 +3
# print(tk)
# t=np.arange(ti,tf, 0.001)
# y = np.piecewise(t,t>0,[1])
# def u(t): return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
# def f(t): return  np.flip((t-tk)*(u(t-tk)-u(t-tl))+3*u(t-tl) )
# plt.plot(t, f(t))
# plt.show()


tf = 20
ti = 5

tl = 3  
tk2 = tl+4
tl2= tk2 +3
print(tk)
t=np.arange(ti,tf, 0.001)
y = np.piecewise(t,t>0,[1])
def u(t): return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
def f(t): return  (t-ti)*(u(t-ti)-u(t-(ti+tl)))+tl*u(t-(ti+tl)) - (t-(tf-3))*(u(t-(tf-3))-u(t-(tf)))-3*u(t-(tf))
plt.plot(t, f(t))
plt.show()
