n, k = map(int, input().split())
C = [0] * k
for n in map(int, input().split()):
    C[n % k] += 1
c = min(C[0], 1)
for i in range(1, k // 2 + 1):
    if i != k - i:
        c += max(C[i], C[k - i])
if k % 2 == 0:
    c += 1
print(c)
