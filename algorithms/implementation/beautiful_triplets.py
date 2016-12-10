n, d = map(int, input().split())
t = list(map(int, input().split()))
print(sum(t[i] + d in t and t[i] + 2 * d in t for i in range(n)))
