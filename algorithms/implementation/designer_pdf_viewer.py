h = list(map(int, input().split()))
w = input().strip()
a = 'abcdefghijklmnopqrstuvwxyz'
l = []
for k in w:
    for i, j in zip(h, a):
        if k == j:
            l.append(i)
print(max(l) * len(w))
