import matplotlib.pyplot as plt
import numpy as np

# Restricciones
# -x + 2y < 8
# x + y < 6

# Creamos un vector x para graficar
x = np.linspace(0, 10, 1000)

# Restricción -x + 2y < 8
y1 = (8 + x) / 2

# Restricción x + y < 6
y2 = 6 - x

# Creamos la gráfica
fig, ax = plt.subplots()

# Graficamos las restricciones
ax.plot(x, y1, label='-x + 2y = 8')
ax.plot(x, y2, label='x + y = 6')

# Agregamos etiquetas y título
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_title('Restricciones')

# Agregamos leyenda
ax.legend()

# Mostramos la gráfica
plt.show()