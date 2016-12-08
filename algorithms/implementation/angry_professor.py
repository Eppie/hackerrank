t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = map(int, input().split())
    print('YES' if sum(x <= 0 for x in a) < k else 'NO')
