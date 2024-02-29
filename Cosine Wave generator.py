import numpy as np
import matplotlib.pyplot as plt

sampling_frequency = 44100 #Change the sampling frequency accordingly

sampling_period = 1/sampling_frequency
t=np.arange(-1.,1.,sampling_period)

A = 1. #Change the amplitude accordingly

f = 2. #Change the frequency accordingly

w= 2*np.pi*f

phi = 0. #Change the phase accordingly

x=A*np.cos(w*t+phi)
fig,ax=plt.subplots()
ax.plot(t,x)
plt.grid(True)
plt.show()

