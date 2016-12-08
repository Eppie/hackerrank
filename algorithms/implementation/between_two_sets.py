input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(len([x for x in range(1, 101) if all(x % a == 0 for a in A) and all(b % x == 0 for b in B)]))
