import matplotlib.pylab as plt
import numpy as np

fig = plt.figure()
fig.suptitle('NO axes on this figure')

fig, ax_list = plt.subplots(2, 2)
