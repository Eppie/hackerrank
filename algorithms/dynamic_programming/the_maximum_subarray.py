def a(l):
    n = -1E5
    m = c = n
    for i in l:
        c = max(c + i, i)
        m = max(m, c)
    s = sum(x for x in l if x > 0)
    if max(l) <= 0:
        s = max(l)
    return '%s %s' % (m, s)

for _ in range(int(input())):
    input()
    print(a(list(map(int, input().split()))))
