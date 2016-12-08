x = list(map(int, input().split()))
print('{} {}'.format(sum(x) - max(x), sum(x) - min(x)))
