m = t = 2
for _ in range(1, int(input())):
    m += m >> 1
    t += m
print(t)
