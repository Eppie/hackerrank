A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = D = 0
for i in range(3):
    if A[i] > B[i]:
        C += 1
    if A[i] < B[i]:
        D += 1
print("{} {}".format(C, D))
