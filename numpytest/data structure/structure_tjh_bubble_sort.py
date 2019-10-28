# 冒泡排序

def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]




li = [10, 44, 20, 17, 77, 31, 93, 55, 53]
bubble_sort(li)
print(li)
