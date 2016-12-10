for _ in range(int(input())):
    n, a, b = int(input()), int(input()), int(input())
    print(' '.join(map(str, sorted({x * a + (n - 1 - x) * b for x in range(n)}))))
