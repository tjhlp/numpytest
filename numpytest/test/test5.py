def bubble(alist):
    for i in range(len(alist) - 1, 0, -1):
        for t in range(i):
            if a[t] > a[t + 1]:
                a[t], a[t + 1] = a[t + 1], a[t]
    return alist


a = [11, 333, 2423, 22, 5, 32, 3]
b = bubble(a)
print(b)
