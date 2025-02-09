import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import Practica4_Ej1y2 as Ej2
from mpl_toolkits.mplot3d import Axes3D

def data(i, z, line):
    z = np.cos(x+y+i)
    ax.clear()
    line = ax.plot_surface(x, y, z,color= 'b')
    return line,

n = 2.*np.pi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0,n,100)
y = np.linspace(0,n,100)
x,y = np.meshgrid(x,y)
z = np.cos(x+y)
line = ax.plot_surface(x, y, z,color= 'b')

ani = animation.FuncAnimation(fig, data, fargs=(z, line), interval=30, blit=False)

plt.show()
