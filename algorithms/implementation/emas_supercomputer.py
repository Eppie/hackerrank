from itertools import chain, combinations, repeat
N, M = map(int, input().split())
g = [[c == 'G' for c in input().strip()] for _ in range(N)]


def V(x, y):
    c = set()
    for e in chain([[(x, y)]], zip(zip(range(x + 1, N), repeat(y)), zip(reversed(range(x)), repeat(y)), zip(repeat(x), range(y + 1, M)), zip(repeat(x), reversed(range(y))))):
        if all(g[i][j] for i, j in e):
            c.update(e)
            yield frozenset(c)
        else:
            return
p = chain.from_iterable(V(i, j) for i in range(N) for j in range(M))
m = -1
for q, r in combinations(p, 2):
    if not q & r:
        m = max(m, len(q) * len(r))
print(m)
