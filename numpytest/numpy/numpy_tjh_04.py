d = {'a': 10, 'b': 9, 'c': 3, 'd': 18}
a = sorted(d.items(), key=lambda x: x[1])
print(a)
