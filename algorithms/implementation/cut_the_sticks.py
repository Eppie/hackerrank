input()
A = list(map(int, input().split()))
while 1:
    m = min(A)
    print(len(A))
    for i in range(len(A)):
        A[i] = A[i] - m
        if A[i] <= 0:
            A[i] = 0
    for i in range(A.count(0)):
        A.remove(0)
