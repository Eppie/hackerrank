l = int(input())
r = int(input())
print(max([A ^ B for A in range(l, r + 1) for B in range(l, r + 1)]))
