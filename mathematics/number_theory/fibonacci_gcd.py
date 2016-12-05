from functools import reduce


def G(a, b):
    while b:
        a, b = b, a % b
    return a
mem, m = {0: 1, 1: 1}, 1000000007


def F(n):
    if n in mem:
        return mem[n]
    k = n // 2
    if n & 1:
        mem[n] = (F(k) * F(k + 1) + F(k - 1) * F(k)) % m
    else:
        mem[n] = (F(k) * F(k) + F(k - 1) * F(k - 1)) % m
    return mem[n]

print(F(reduce(G, [int(input()) for _ in range(int(input()))]) - 1))
