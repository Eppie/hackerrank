for i in range(int(input())):
    A, B, C = map(int, input().split())
    a = 0
    w = 0
    while A > 0 and A >= B:
        A -= B
        a += 1
        w += 1
        a, w = [(a, w), (a + 1, 1)][w == C]
    print(a)
