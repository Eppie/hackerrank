from math import *
for _ in range(int(input())):
    A, B = map(int, input().split())
    print(int(sqrt(B)) - ceil(sqrt(A)) + 1)
