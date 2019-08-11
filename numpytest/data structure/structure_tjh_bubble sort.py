# 冒泡排序

def bubble_sort(alist):
    for j in range(len(alist) - 1, 0, -1):
        print(j)
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def bubble_sort_reverse(alist):
    for j in range(len(alist)):
        for i in range(j):
            pass


li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort_reverse(li)
print(li)
