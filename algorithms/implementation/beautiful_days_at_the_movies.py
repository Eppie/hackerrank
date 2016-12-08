i, j, k = map(int, input().split())
print(sum(abs(a - int(str(a)[::-1])) % k == 0 for a in range(i, j + 1)))
