import numpy as np 
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from scipy import signal as sp

# ti = -5
# tf = 0
# a = (tf-ti)
# c = (tf - ti)/100
# tll = int(np.linspace(ti,ti+a,c))
# x= (((tll-ti)-a)**2)/(a)
# tl2 = int(np.linspace(ti+a,ti+a+a,c))
# y = (-((tl2-ti)-(a+a))**2)/(a +a) 
# tl3 = int(np.linspace(ti+a+a, tf-a,c))
# z = (((tl3-ti)-(a+a+a))**2)/(a ) 
# tl4 = int(np.linspace(tf-a,tf,c))
# w = (-((tl4-ti)-(a+a+a+a))**2)/(a +a )
# t = np.concatenate(tll,tl2,tl3)
# h = np.concatenate(x,y,z)
# plt.plot(t,h)
# plt.show()

ti =5
tf = 10
ds  = 0.001
a = tf -ti


t = np.arange(ti,tf, ds )
conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
pieces = np.piecewise(t, conds, funcs)
plt.plot(t,pieces)
plt.show()

plt.plot(t, np.flip(pieces))
plt.show()


