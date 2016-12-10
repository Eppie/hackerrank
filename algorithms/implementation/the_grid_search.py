def p(G, a, b, P, r, c):
    m, d = 1, 0
    for i in range(a, a + r):
        e = 0
        for j in range(b, b + c):
            if G[i][j] != P[d][e]:
                m = 0
                break
            e += 1
        d += 1
        if not m:
            break
    return m

for _ in range(int(input())):
    R, C = map(int, input().split())
    G = [input() for _ in range(R)]
    r, c = map(int, input().split())
    P = [input() for _ in range(r)]
    m = 0
    for a in range(R - r + 1):
        for b in range(C - c + 1):
            if G[a][b] == P[0][0]:
                m = p(G, a, b, P, r, c)
                if m:
                    break
        if m:
            break
    print(['NO', 'YES'][m])
