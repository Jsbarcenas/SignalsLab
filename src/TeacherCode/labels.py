<<<<<<< HEAD
# # Graficas de funciones singulares
# # from matplotlib.pyplot import *
# # from numpy import *

# # # funcion escalon unitario
# # def u(t): return piecewise(t,[t<0.0,t>=0.0],[0,1])

# # # funcion f(t)
# # def f(t): return t*(u(t)-u(t-1))+2*u(t-1)
 
# # t=linspace(-1,5,1000)
# # plot(t,f(t),'k',label=r'$f(t)$',lw=2)
# # xlim(-1,3);ylim(0,2.2)
# # legend(loc='best')
# # title(r'Funci\'on $f(t)=tu(t)-(t-1)u(t-1)+u(t-1)$')
# # show()

# # import numpy as np
# # from matplotlib import pyplot as plt
# # def ut(t):
# #  return t*np.arange(0,5)


# # t = np.arange(0,10,0.001)
# # f= np.piecewise(t, t>0, [ut(5),0])
# # plt.plot(t,f)
# # plt.show()

# # Señales modelo varias
# import numpy as np
# from matplotlib import pyplot as plt
# from scipy import signal as sp

# # tf = 6
# # ti = -8
# # tk = tf -ti


# # t=np.arange(ti,tf, 0.001)
# # y = np.piecewise(t,t>0,[1])
# # def u(t): return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
# # def f(t): return  (t-(tk/3 + (ti)))*(u(t-(tk/3+(ti)))-u(t-(tk*2/3 + (ti))))+(tk/3)*u(t-(tk*2/3 + (ti))) 
# # plt.plot(t, f(t))
# # plt.show()


# # tf = 30
# # ti = -22

# # tk = tf -ti

# # print(tk)
# # t=np.arange(ti,tf, 0.001)
# # y = np.piecewise(t,t>0,[1])
# # def u(t): return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
# # def f(t): return  np.flip ((t-(tk/3 + (ti)))*(u(t-(tk/3+(ti)))-u(t-(tk*2/3 + (ti))))+(tk/3)*u(t-(tk*2/3 + (ti))) )
# # plt.plot(t, f(t))
# # plt.show()






# tf = 4
# ti = 0
# td = tf -ti
# tk = 0
# tl = 3  
# tk2 = tl+4
# tl2= tk2 +3
# print(tk)
# t=np.arange(ti,tf, 0.001)
# y = np.piecewise(t,t>0,[1])
# def u(t): return np.piecewise(t,[t<0.0,t>=0.0,],[0,1])
# def f(t): return  (t)*(u(t)-u(t-tl))+tl*u(t-tl)          -         (t-(tf-3))*(u(t-(tf-3))-u(t-(tf)))-3*u(t-(tf))
# plt.plot(t, f(t))
# plt.show()



# t = np.arange(-10,10,0.001)

# ge =-1* (2*(t**2))+t*2

# plt.plot(t,np.flip(ge))
# plt.show()

import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def showConvolution(f1, f2, t0):
    # Calculate the overall convolution result using Simpson integration
    convolution = np.zeros(len(t))
    for n, t_ in enumerate(t):
        prod = lambda tau: f1(tau) * f2(t_-tau)
        convolution[n] = scipy.integrate.simps(prod(t), t)

    # Create the shifted and flipped function
    f_shift = lambda t: f2(t0-t)
    prod = lambda tau: f1(tau) * f2(t0-tau)

    # Plot the curves
    plt.gcf().clear() # il

    plt.subplot(211)
    plt.gca().set_ymargin(0.05) # il
    plt.plot(t, f1(t), label=r'$f_1(\tau)$')
    plt.plot(t, f_shift(t), label=r'$f_2(t_0-\tau)$')
    plt.fill(t, prod(t), color='r', alpha=0.5, edgecolor='black', hatch='//') # il
    plt.plot(t, prod(t), 'r-', label=r'$f_1(\tau)f_2(t_0-\tau)$')
    plt.grid(True); plt.xlabel(r'$\tau$'); plt.ylabel(r'$x(\tau)$') # il
    plt.legend(fontsize=10) # il
    plt.text(-4, 0.6, '$t_0=%.2f$' % t0, bbox=dict(fc='white')) # il

    # plot the convolution curve
    plt.subplot(212)
    plt.gca().set_ymargin(0.05) # il
    plt.plot(t, convolution, label='$(f_1*f_2)(t)$')

    # recalculate the value of the convolution integral at the current time-shift t0
    current_value = scipy.integrate.simps(prod(t), t)
    plt.plot(t0, current_value, 'ro')  # plot the point
    plt.grid(True); plt.xlabel('$t$'); plt.ylabel('$(f_1*f_2)(t)$') # il
    plt.legend(fontsize=10) # il
    plt.show() # il

Fs = 50  # our sampling frequency for the plotting
T = 5    # the time range we are interested in
t = np.arange(-T, T, 1/Fs)  # the time samples
f1 = lambda t: np.maximum(0, 1-abs(t))
f2 = lambda t: (t>0) * np.exp(-2*t)

t0 = np.arange(-2.0,2.0, 0.05)

fig = plt.figure(figsize=(8,3))
anim = animation.FuncAnimation(fig, showConvolution(f1,f2, t0), frames=np.linspace(0, 50, 500), interval=80)

anim.save('animation.mp4', fps=30) # fps = frames per second

plt.show()
=======
if selectF1Lab.get() == 'Sustentation1':
        t = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        tf = float(timeFinalF1Entry.get())
        ti =float(timeInitF1Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = pieces
        plotF1TimeGeneratorStatus =  t
        plotF1GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)
    if selectF1Lab.get() == 'Sustentation2':
        t = np.arange(float(timeInitF1Entry.get()),float(timeFinalF1Entry.get()),ts)
        tf = float(timeFinalF1Entry.get())
        ti =float(timeInitF1Entry.get())
        a = tf -ti
        conds = [(t <= ti+a/4) & (t>=ti), (t >= ti+a/4) & (t <= ti+2*a/4), (t > ti+2*a/4) & (t < ti+ 3*a/4) , (t >= ti+3*a/4) & (t <= ti+a)]
        funcs = [lambda t: (((t-(ti+a/4))**2)/(1))  ,
        lambda t: (-((t- (ti+2*a/4))**2)/(1)) + (a/4)**2,
        lambda t: (((t-(ti+3*a/4))**2)/(1)),
        lambda t: (-((t- (ti+a))**2)/(1)) + (a/4)**2]
        pieces = np.piecewise(t, conds, funcs)
        sustentGenerator = np.flip(pieces)
        plotF1TimeGeneratorStatus =  t
        plotF1GeneratorStatus = sustentGenerator
        canvasChange()
        print(sustentGenerator)
>>>>>>> bf409c022f4cabb41605878905b9a38bc352c8fd
