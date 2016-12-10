n, m = map(int, input().split())
cl = sorted(map(int, input().split()))
print(max([0, cl[0], n - 1 - cl[-1]] + [(cl[i] - cl[i - 1]) // 2 for i in range(1, m)]))
