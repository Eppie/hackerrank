print((lambda x, y: 100 - sum(1 + 2 * y[i] for i in range(0, x[0], x[1])))(list(map(int, input().split())), list(map(int, input().split()))))
