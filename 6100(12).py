import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

ax = fig.add_subplot(projection='3d')

x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                     np.arange(-0.8, 1, 0.2),
                     np.arange(-0.8, 1, 0.8))

u = 0
v = y**2
w = -2*y*z - y

ax.quiver(x, y, z, u, v, w, length=0.1)
ax.axis('off')

plt.show()