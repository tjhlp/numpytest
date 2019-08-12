def select_sort(alist):
    count = len(alist)

    for i in range(count):
        min_index = i
        for j in range(i+1, count):
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


li = [10, 44, 20, 17, 77, 31, 93, 55, 53]
select_sort(li)
print(li)







