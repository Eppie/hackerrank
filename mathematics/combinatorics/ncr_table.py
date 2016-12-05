def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

for _ in range(int(input())):
    n = int(input())
    c = ' '.join([str(choose(n, k) % 10**9) for k in range(n + 1)])
    print(c)
