n = int(input())
c = list(map(int, input().split()))
c.insert(n, 0)
D = 0
i = 0
while i < n - 1:
    i += (c[i + 2] == 0) + 1
    D += 1
print(D)
