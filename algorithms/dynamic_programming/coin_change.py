n = int(input().split()[0])
C = map(int, input().split())
w = [0] * -~n
w[0] = 1
for c in C:
    for j in range(c, n + 1):
        w[j] += w[j - c]
print(w[n])
