import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5 * np.cos(2 * x)

x = np.linspace(0, 2 * np.pi, 100)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function f(x) = sin(x) + 0.5*cos(2x)')
plt.grid(True)
plt.show()