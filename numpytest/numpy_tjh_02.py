"""
  numpy 中 ndarrays 创建
"""
import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])
b = np.array((0, 1, 2, 3, 4, 5))
# 创建一个0到3的数组
# np.arange(3)
#       》》》array([0, 1, 2])
c = np.arange(3)
# >>> np.linspace(2.0, 3.0, num=5)
#     array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
#     >>> np.linspace(2.0, 3.0, num=5, endpoint=False)
#     array([ 2. ,  2.2,  2.4,  2.6,  2.8])
#     >>> np.linspace(2.0, 3.0, num=5, retstep=True)
#     (array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
d = np.linspace(2, 3, num=4)
print(a)
print(b)
print(c)
print(d)

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
print(type(a))
print(a.dtype)
print(a.size)
print(a.itemsize)
