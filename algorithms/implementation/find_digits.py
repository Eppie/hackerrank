for _ in range(int(input())):
    n = input()
    print(sum([d and int(n) % d == 0 for d in map(int, n)]))
