for _ in range(int(input())):
    r = 1
    for i in range(1, int(input()) + 1):
        if i % 2:
            r *= 2
        else:
            r += 1
    print(r)
