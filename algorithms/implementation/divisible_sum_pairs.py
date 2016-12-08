n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
print(sum((i + j) % k == 0 for x, i in enumerate(a) for j in a[x + 1:]))
