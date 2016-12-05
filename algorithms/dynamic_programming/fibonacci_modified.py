def run(n):
    if n not in t:
        t[n] = run(n - 2) + (run(n - 1) ** 2)
    return t[n]

t1, t2, n = map(int, input().split())
t = {1: t1, 2: t2}
print(run(n))
