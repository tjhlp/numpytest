"""
    numpy 加减乘除
"""
import numpy as np

num_a = np.array([[0, 1], [2, 3]])
num_b = np.array([[4, 5], [6, 7]])

# 矩阵运算
sum_matrix = num_a + num_b
difference_matrix = num_a - num_b
# product_matrix = num_a * num_b
product_matrix = num_a.dot(num_b)
quotient_matrix = num_a / num_b

print(sum_matrix)
print('-' * 50)
print(difference_matrix)
print('-' * 50)
print(product_matrix)
print('-' * 50)
print(quotient_matrix)
