def P(n):
    s = [1] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if s[i]:
            s[i * i::2 * i] = [0] * ((n - i * i - 1) // (2 * i) + 1)
    return len([i for i in [2] + [i for i in range(3, n, 2) if s[i]] if i < n])


def C(n, k):
    if 0 <= k <= n:
        a = b = 1
        for t in range(1, min(k, n - k) + 1):
            a *= n
            b *= t
            n -= 1
        return a // b
    return 0

for _ in range(int(input())):
    N, W = int(input()), 1
    for s in range(N // 4 + 1):
        W += C(N - s * 4 + s, s)
    print(P(W))
