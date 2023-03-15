import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(-1, 1, 100)
U, V = np.meshgrid(u, v)

#First
x1 = 3 * np.outer(np.cos(u), np.sin(v))
y1 = 3 * np.outer(np.sin(u), np.sin(v))
z1 = np.outer(0,0)

#Second
x2 = 0.2 * np.cosh(V) * np.cos(U)
y2 = 0.2 * np.cosh(V) * np.sin(U)
z2 = 1.6 * np.sinh(V) + 1.9

#Third
x3 = 3.25 * np.sinh(V) * np.cos(U)
y3 = 3.25 * np.sinh(V) * np.sin(U)
z3 = 2.9 * np.cosh(V) + 0.9

#Fourth
x4 = 3.8 * V * np.cos(U)
y4 = 3.8 * V * np.sin(U)
z4 = 9 * np.sqrt(1 - V**2) + 5.4

# Plot the surface
ax.plot_surface(x1, y1, z1, cmap='magma')
ax.plot_surface(x2, y2, z2, cmap='magma')
ax.plot_surface(x3, y3, z3, cmap='magma')
ax.plot_surface(x4, y4, z4, cmap='magma')

# set the axis labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 6)

plt.show()