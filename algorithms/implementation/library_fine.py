a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
g = 0
if c > f:
    g = 10000
elif c == f:
    if b > e:
        g = (b - e) * 500
    elif b == e:
        if a > d:
            g = (a - d) * 15
print(g)
