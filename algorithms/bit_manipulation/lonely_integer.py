input()
b = input().split()
r = 0
for i in b:
    r ^= int(i)
print(r)
