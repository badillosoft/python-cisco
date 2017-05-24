a = [5, 2, 1, 2, 3, 4]
ac = a[:]
b = []

for k in range(0, len(a)):
    m = None

    for x in a:
        if m == None or x < m:
            m = x

    # m = min(a)

    i = a.index(m)

    a.pop(i)

    # a.remove(m)

    b.append(m)

print ac
print b

for i in range(0, len(a)):
    m = min(a)
    a.remove(m)
    b.append(m)