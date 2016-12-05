n = int(input())
a = list(map(int, [input() for _ in range(n)]))
c = [1] * n
d = []
for i in range(1, n):
    if a[i] < a[i - 1]:
        if not d:
            d = [i - 1]
        d.append(i)
        if not i == n - 1:
            continue
    if a[i] > a[i - 1]:
        c[i] = c[i - 1] + 1
    if d:
        for e, i in enumerate(d[::-1]):
            c[i] = max(c[i], e + 1)
        del d[:]
print(sum(c))
