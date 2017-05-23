a = [1, 1, 2, 3, 5, 8, 13, 21, 34]

for x in a:
    print x

# range(n) => [0, 1, 2, ..., n - 1]
# range(a, b) => [a, a + 1, a + 2, ..., b - 1]
# range(a, b, s) => [a, a + s, a + 2 * s, a + 3 * s, ..., b - 1]

for i in range(len(a)):
    print a[i]