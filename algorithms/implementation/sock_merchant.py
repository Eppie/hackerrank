input()
s = input().split()
print(sum(s.count(e) // 2 for e in set(s)))
