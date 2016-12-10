for _ in range(int(input())):
    s = list(input())
    p = next((i - 1 for i in range(len(s) - 1, 0, -1) if s[i - 1] < s[i]), None)
    if p == None:
        print("no answer")
    else:
        rs = next(i for i in range(len(s) - 1, 0, -1) if s[i] > s[p])
        s[p], s[rs] = s[rs], s[p]
        print(''.join(s[:p + 1] + list(reversed(s[p + 1:]))))
