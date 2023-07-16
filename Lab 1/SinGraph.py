import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5 * np.pi, 0.00001)
y = np.sin(x)
plt.title("Sin Graph")
plt.plot(x, y)
plt.show()
