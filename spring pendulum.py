import numpy as np
from numpy import sin, cos
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation
L0,k,m,g=1,40,1,9.81
t = np.arange(0, 40, dt)
initial_state=(3*np.pi/4,0,L0,0)
def derivs(state, t):        
"""Returns[theta_dot, theta_double_dot, L_dot, L_double_dot]"""
theta_double_dot=(-g*np.sin(theta)-2*theta_dot*L_dot)/L
L_double_dot=(m*L*theta_dot**2-k*(L-L0)+m*g*np.cos(theta))/m
y = integrate.odeint(derivs, initial_state, t)
theta, L = y[:,0], y[:,2]
x = L * np.sin(theta)
y = -L * np.cos(theta)
fig, ax = plt.subplots(subplot_kw= {'xlim' : (-4, 4), 'ylim' :(-4.5, 4)})
ax.grid()
ax.set_aspect('equal')
line, = ax.plot([], [], 'o-', lw=2, color='#e63946')
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
line.set_data([], [])
time_text.set_text('')
def animate(i):
    x_value = [0, x[i]]
    y_value = [0, y[i]]
    line.set_data(x_value, y_value)
    time_text.set_text( f'Time={i*dt:0.1f}s')              
    return line, time_text

ani = animation.FuncAnimation(fig, animate, range(1, len(y), 2),
                              interval=dt*700,  blit=True)
ax.annotate(s = "Simulation of a spring pendulum", xy=(0.28, 0.05), xycoords='figure fraction', fontsize=13);
plt.subplots_adjust(bottom=0.15)
plt.show()
fig, ax = plt.subplots()
ax.plot(x, y, 'teal')
ax.plot(0, 0, 'o', ms = 6, color='black')
ax.axhline(0,  linewidth=1)
ax.annotate(s = "Chaotic Behaviour", xy=(0.37, 0.04), xycoords='figure fraction', fontsize=13)
ax.annotate(s = "y = 0", xy=(0.91, 0.70), xycoords='figure fraction', fontsize=13)
plt.subplots_adjust(bottom = 0.15)
plt.show()
