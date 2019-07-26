import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-1, 1, 50)
print(x)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y1, label='linear')
plt.plot(x, y2, label='cubic')

plt.xlabel('x label')
plt.xlabel('y label')
plt.show()
