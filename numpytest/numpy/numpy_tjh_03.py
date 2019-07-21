import numpy as np

"""三个不同维数的数组"""

# 1D array
print(np.arange(6))
# 2D array
print(np.arange(12).reshape(4, 3))
# 3D array
print(np.arange(24).reshape(2, 3, 4))

# ndarry 通用函数

a = np.random.random((2,3))
print(a)
print()
print(a.sum())
print(a.max())
print(a.min())