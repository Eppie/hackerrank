input()
b = map(int, input().split())
s = c = 0
for x in b:
    c = (c + x) % 2
    s += c * 2
print([s, 'NO'][c])
