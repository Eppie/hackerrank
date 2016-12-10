n = int(input())
G = []
for _ in range(n):
    G.append(list(input().strip()))
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if G[i][j] > max(G[i - 1][j], G[i + 1][j], G[i][j - 1], G[i][j + 1]):
            G[i][j] = 'X'
for i in range(n):
    print(''.join(G[i]))
