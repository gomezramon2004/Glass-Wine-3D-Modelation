
# Se importan las librerías esenciales para el proyecto.
# MatplotLib agrega la capacidad para gráficar ecuaciones.
# Numpy da licencia al uso de métodos númericos y fórmulas trigonométricas de manera más amplia y sencilla.
# Axes3D es un toolkit de MatplotLib, que hace posible el uso de modelación en un espacio tridimensional.
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Se crea el espacio tridimensional con su respectivo tamaño y dimensión, también se crean las variables u y v que crearán un array de cien números; uno desde -pi a pi y otro de -1 a 1.
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(-np.pi, np.pi, 100)
v = np.linspace(-1, 1, 100)
U, V = np.meshgrid(u, v)

# Primera figura: Círculo.
x1 = 3 * np.outer(np.cos(u), np.sin(v))
y1 = 3 * np.outer(np.sin(u), np.sin(v))
z1 = np.outer(0,0)

# Segunda figura: Hiperboloide de una hoja.
x2 = 0.2 * np.cosh(V) * np.cos(U)
y2 = 0.2 * np.cosh(V) * np.sin(U)
z2 = 1.6 * np.sinh(V) + 1.9

# Tercera figura: Elipsoide.
x3 = 3.25 * np.sinh(V) * np.cos(U)
y3 = 3.25 * np.sinh(V) * np.sin(U)
z3 = 2.9 * np.cosh(V) + 0.9

# Cuarta figura: Hiperboloide de dos hojas.
x4 = 3.8 * V * np.cos(U)
y4 = 3.8 * V * np.sin(U)
z4 = 9 * np.sqrt(1 - V**2) + 5.4

#  Métodos que crean la figura tridimensional en base a las ecuaciones implicitas dadas por la parametrización, agregandole un tono magma en su estética superficial.
ax.plot_surface(x1, y1, z1, cmap='magma')
ax.plot_surface(x2, y2, z2, cmap='magma')
ax.plot_surface(x3, y3, z3, cmap='magma')
ax.plot_surface(x4, y4, z4, cmap='magma')

# Métodos que agregan etiquetas para diferenciar y limitar los respectivos ejes.
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 6)

# Método que muestra el plot en una ventana.
plt.show()
