m = n = int(input())
A, d = list(map(int, input().split())), {}
for i in range(n):
    try:
        m = min(i - d[A[i]], m)
        if m == 1:
            break
    except:
        pass
    d[A[i]] = i
print(-1 if m == n else m)
