n, m = map(int, input().split())
p = [int(input(), 2) for _ in range(n)]
P = [bin(p[i] | p[j]).count('1') for i in range(n) for j in range(i, n)]
Q = max(P)
print(Q)
print(P.count(Q))
