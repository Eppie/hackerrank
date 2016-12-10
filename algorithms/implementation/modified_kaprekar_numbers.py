a = int(input())
b = int(input())
n = []
for i in range(b + 1):
    c = str(i ** 2)
    l = len(c) // 2
    d = 0 if c[:l] == '' else int(c[:l])
    e = [int(c[l:]), 0][c[l:] == '']
    if d + e == i and i >= a:
        n.append(i)
if n:
    for i in n:
        print(i, end=' ')
else:
    print('INVALID RANGE')
