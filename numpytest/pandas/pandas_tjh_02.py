import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
fig = plt.figure(figsize=(3, 6))  # 指定画图区大小（长，宽）
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(np.random.randint(1, 5, 5), np.arange(5))  # 第一个子图画图
ax2.plot(np.arange(10) * 3, np.arange(10))  # 第二个子图画图
plt.show()
