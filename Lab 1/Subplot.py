import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = x + 10
plt.subplot(3, 1, 1)
plt.title("G1")
plt.legend(loc=2)
plt.plot(x, y)
plt.subplot(3, 1, 2)
plt.title("G2")
plt.plot(x + 10, y + 20)
plt.subplot(3, 1, 3)
plt.title("G3")
plt.plot(x + 50, y + 100)
plt.subplots_adjust(hspace=1)

plt.show()