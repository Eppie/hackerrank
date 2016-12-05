n = int(input())
a = []
for a_i in range(n):
    a_t = list(map(int, input().split()))
    a.append(a_t)

p1 = p2 = 0
for i in range(n):
    p1 += a[i][i]
    p2 += a[i][-1 - i]
print(abs(p2 - p1))
