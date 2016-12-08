for _ in range(int(input())):
    N, M, S = list(map(int, input().split()))
    print(((S - 1 + M - 1) % N) + 1)
