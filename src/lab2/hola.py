import numpy as np 
from tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from scipy import signal as sp

ti_x=-5
tf_x=3

ti_h=0

tf_h=6

ts = 0.1

tx=np.arange(ti_x,tf_x+ts,ts)
th=np.arange(ti_x,tf_h+ts,ts)
x = (4/5)**(tx)
h = (8/9)**(th)

lx= len(tx)
lh = len(th)

Lx_temp = int(len(tx)*ts)
Lh_temp = int(len(th)*ts)

eje = np.arange(ti_x - Lh_temp,tf_x+Lh_temp,ts)
x_n = np.concatenate((np.zeros(lh),x,np.zeros(lh)))
h_n = np.concatenate((np.zeros(lh),h,np.zeros(lx)))


plt.ion()
plt.figure()


tx=ty1

x_new=np.zeros(int((b-a)*fs ))


for i in range(len(x)):
    x_new[(i+int(pi_x*fs)+int((-a)*fs))]=x[i]


for i in range(frames):

    plt.clf()
    plt.subplot(2,1,1)
    for k in range(len(h)):
        h_new[k+i +int((-a)*fs)-len(h)+int(pi_x*fs)] = h[k]

        
    plt.plot(th1,h_new)
    plt.plot(tx,x_new)
    h_new=np.zeros(int((b-a)*fs))
   
    plt.grid()
        
        
    if i<len(y):
        y_new[i+int(min(ty)*fs)+ int(((-a)*fs))]= y[i]

    plt.subplot(2,1,2)
    plt.plot(ty_new, y_new)
   

    
   

    
       
    plt.show()
    plt.pause(0.001)
  
    if i==frames-1:
        plt.ioff()

plt.show()