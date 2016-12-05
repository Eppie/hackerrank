n = int(input())
arr = list(map(int, input().split()))
pos = neg = zero = 0
for e in arr:
    if e > 0:
        pos += 1
    elif e < 0:
        neg += 1
    else:
        zero += 1
print(pos / n)
print(neg / n)
print(zero / n)
