from itertools import count, zip_longest
_, k = map(int, input().split())
A = list(map(int, input().split()))
P = count(1)
print(sum([len([1 for p in zip_longest(*[iter(range(1, a + 1))] * k) if next(P) in p]) for a in A]))
