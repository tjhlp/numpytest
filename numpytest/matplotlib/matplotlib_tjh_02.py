import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-1, 1, 50)
print(x)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure(num=1)
# image
plt.plot(x, y1, label='linear')
plt.plot(x, y2, color='red', label='cubic',linestyle='--')
# limit
plt.xlim(-1, 2)
plt.ylim(-2, 3)
ticks = np.linspace(-1,2,5)
plt.xticks(ticks)
plt.yticks([-2, -1, 1, 2],
           [r'$really\ bad$', '$bad$', '$well$', '$really\ well$']
           )
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.legend(loc='best')
plt.show()
